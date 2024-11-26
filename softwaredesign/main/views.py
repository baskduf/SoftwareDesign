from django.shortcuts import render
from aiservice.models import AI

from django.conf import settings
# Create your views here.

def about(request):    # BASE_DIR을 사용하여 README.md 파일 경로 설정
    return render(request, 'about.html')

def index(request):
    
    ai_objects = AI.objects.all().order_by('-created_at')
    return render(request, "index.html",{'ai_objects': ai_objects})


