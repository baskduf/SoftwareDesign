from django.shortcuts import render, get_object_or_404

from .models import AI

def index(request, ainame):
    # AI 모델에서 ainame과 일치하는 객체를 가져옴
    ai = get_object_or_404(AI, ainame=ainame)
    
    # 템플릿에 AI 데이터를 넘겨줌
    return render(request, 'ai/ai_detail.html', {'ai': ai})