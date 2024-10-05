from django.shortcuts import render
from .forms import createAIForm
# Create your views here.
from authentication.models import AI

def index(request):
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

                # 만약 사용자가 프롬프트를 입력하지 않았을 경우, 기본 프롬프트 설정
                if not prompt:
                    if personality == 'calm':
                        prompt = "차분하게 사용자와 대화하세요."
                    elif personality == 'active':
                        prompt = "활기차고 적극적으로 사용자와 대화하세요."
                    elif personality == 'tsundere':
                        prompt = "츤데레처럼 약간은 투덜대면서도 도와주는 태도로 사용자와 대화하세요."
                    elif personality == 'playful':
                        prompt = "장난스럽게 사용자와 대화를 이어가세요."
                    elif personality == 'mysterious':
                        prompt = "신비로운 분위기를 유지하며 사용자와 대화하세요."
                    elif personality == 'intelligent':
                        prompt = "지적인 어조로 사용자의 질문에 답하세요."


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
