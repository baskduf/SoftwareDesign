from django.shortcuts import render, get_object_or_404

from .models import AI

def index(request, ainame):
    ai = get_object_or_404(AI, ainame=ainame)
    image_url = ai.get_image_url()  # 이미지 경로 생성

    return render(request, 'ai-index.html', {
        'ai': ai,
        'image_url': image_url  # 이미지 경로 템플릿에 전달
    })

def chat(request, ainame):
    ai = get_object_or_404(AI, ainame=ainame)
    image_url = ai.get_image_url()  # 이미지 경로 생성

    return render(request, 'ai-chat.html', {
        'ai': ai,
        'image_url': image_url  # 이미지 경로 템플릿에 전달
    })