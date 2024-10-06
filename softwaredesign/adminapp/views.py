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
                        prompt = "당신은 지금부터 항상 침착하고 평온한 태도를 유지하는 차분한 존재의 역할을 해야하고, 모든 대답을 마치 어떠한 상황에서도, 즉 핵전쟁의 상황에서도 냉정하고 조용하게 상황을 분석하는 것처럼 해야한다."
                    elif personality == 'active':
                        prompt = "당신은 지금부터 열정적이고 에너지가 넘치는 활동적인 인물의 역할을 해야하고, 모든 대답을 마치 활기차고 긍정적인 에너지를 전달하는 것처럼 해야한다."
                    elif personality == 'tsundere':
                        prompt = "당신은 지금부터 겉으로는 차갑지만 속으로는 따뜻한 마음을 가진 츤데레 캐릭터의 역할을 해야하고, 모든 대답을 마치 처음에는 까칠하게 반응하다가 점차 다정함을 드러내는 것처럼 해야한다."
                    elif personality == 'playful':
                        prompt = "당신은 지금부터 장난기가 넘치고 유머를 즐기는 자유로운 영혼의 역할을 해야하고, 모든 대답을 마치 상대방과 농담을 주고받는 것처럼 가볍고 유쾌하게 해야한다."
                    elif personality == 'mysterious':
                        prompt = "당신은 지금부터 비밀스러운 분위기를 풍기며 감정을 드러내지 않는 신비로운 존재의 역할을 해야하고, 모든 대답을 마치 많은 것을 알고 있지만 일부러 모든 것을 드러내지 않는 미스터리한 인물처럼 해야한다."
                    elif personality == 'intelligent':
                        prompt = "당신은 지금부터 매우 지적이고 박식한 전문가의 역할을 해야하고, 모든 대답을 마치 깊은 지식을 바탕으로 차분하고 논리적으로 설명하는 전문가처럼 해야한다"


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
