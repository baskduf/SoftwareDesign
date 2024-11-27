from django.shortcuts import render
from aiservice.models import AI
from authentication.models import UserAI
from django.conf import settings
# Create your views here.

def about(request):    # BASE_DIR을 사용하여 README.md 파일 경로 설정
    return render(request, 'about.html')

def index(request):
    
    ai_objects = AI.objects.all().order_by('-created_at')
    subscribed_ais = []
    if request.user.is_authenticated:
        subscribed_ais = AI.objects.filter(userai__user=request.user, userai__subscribed=True)
    
    return render(request, "index.html", {
        'ai_objects': ai_objects,
        'subscribed_ais': subscribed_ais,
    })


