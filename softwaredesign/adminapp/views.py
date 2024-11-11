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

# myapp/views.py
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import createAIForm
import os
from django.conf import settings
from authentication.models import AI

def create(request):
    # 사용자가 슈퍼유저가 아닌 경우 접근 금지 응답 반환
    if not request.user.is_authenticated or not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_superuser:

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
                    # static 디렉토리의 절대 경로를 얻습니다.
                    # static 디렉토리의 절대 경로를 얻습니다.
                    static_dir = os.path.join(settings.BASE_DIR, 'static', 'img')
                    
                    # 파일 확장자 추출
                    _, ext = os.path.splitext(image.name)  # 확장자를 추출합니다.

                    # 파일 이름 설정 (ainame + 확장자)
                    file_name = f'{ainame}{ext}'
                    
                    # 파일 저장 경로 설정
                    file_path = os.path.join(static_dir, file_name)

                    # 파일 저장 경로를 사용하여 추가 작업을 수행할 수 있습니다.
                    print(f'Image saved to: {file_path}')
                    with open(file_path, 'wb') as f:
                        for chunk in image.chunks():
                            f.write(chunk)
                    
                    ai_instance = AI(ainame=ainame, prompt=prompt, description=description, personality=personality)
                    ai_instance.save()

                    print(f'Image saved to: {file_path}')

                # 데이터 저장 또는 다른 처리를 수행
                # 예를 들어, 데이터베이스에 저장하거나 다른 API 호출 등을 할 수 있습니다.
                # ...


                return redirect('/')  # 성공 페이지로 리다이렉트
    else:
        form = createAIForm()

    return render(request, 'admin-create.html', {'form': form})
