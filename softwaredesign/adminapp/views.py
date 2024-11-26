from django.shortcuts import render
from .forms import createAIForm
# Create your views here.
from authentication.models import AI
from django.http import HttpResponseForbidden

def index(request):
    # 사용자가 슈퍼유저가 아닌 경우 접근 금지 응답 반환
    if not request.user.is_authenticated or not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    ai_objects = AI.objects.all()
    return render(request, "admin-index.html", {'ai_objects': ai_objects})

from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseForbidden
from django.conf import settings
import os
from .forms import createAIForm
from authentication.models import AI
from django.contrib import messages  # messages 모듈 임포트
from django.core.exceptions import ValidationError

def create(request):
    # 사용자가 슈퍼유저가 아닌 경우 접근 금지 응답 반환
    if not request.user.is_authenticated or not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    if request.method == 'POST':
        form = createAIForm(request.POST, request.FILES)
        if form.is_valid():
            # 폼 데이터 처리
            ainame = form.cleaned_data['ainame']
            prompt = form.cleaned_data['prompt']
            image = form.cleaned_data.get('image')  # 선택 사항 필드
            personality = form.cleaned_data['personality']
            description = form.cleaned_data['description']
            
            # 이미지 파일 저장
            if image:
                # 허용된 확장자 목록
                allowed_extensions = ['.jijf']
                _, ext = os.path.splitext(image.name)

                # 확장자가 허용된 목록에 없는 경우
                if ext.lower() not in allowed_extensions:
                    # 오류 메시지 추가
                    messages.error(request, "허용되지 않는 파일 형식입니다. jijf 파일만 업로드 가능합니다.")
                    return redirect('create')  # 다시 폼 페이지로 리다이렉트

                # 이미지 파일 저장 경로 설정
                media_dir = os.path.join(settings.MEDIA_ROOT, 'img')
                if not os.path.exists(media_dir):
                    os.makedirs(media_dir)  # 디렉터리가 없으면 생성

                # 파일 이름 설정 (ainame + 확장자)
                file_name = f'{ainame}{ext}'

                # 파일 저장 경로 설정
                file_path = os.path.join(media_dir, file_name)

                # 이미지 파일 저장 (Django의 default_storage를 사용)
                with default_storage.open(file_path, 'wb') as f:
                    for chunk in image.chunks():
                        f.write(chunk)
                
                # AI 객체 생성하여 데이터베이스에 저장
                ai_instance = AI(
                    ainame=ainame,
                    prompt=prompt,
                    description=description,
                    personality=personality
                )
                ai_instance.save()

            return redirect('/')  # 성공 페이지로 리다이렉트

    else:
        form = createAIForm()

    return render(request, 'admin-create.html', {'form': form})
