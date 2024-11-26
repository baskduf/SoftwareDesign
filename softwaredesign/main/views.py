from django.shortcuts import render
from aiservice.models import AI

from django.conf import settings
import markdown
# Create your views here.

def about(request):    # BASE_DIR을 사용하여 README.md 파일 경로 설정
    readme_path = os.path.join(settings.BASE_DIR, 'README.md')
    
    # README.md 파일이 존재하는지 확인
    if not os.path.exists(readme_path):
        return render(request, 'about.html', {'content': 'README.md 파일을 찾을 수 없습니다.'})
    
    # README.md 파일 읽기
    with open(readme_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # 마크다운을 HTML로 변환
    html_content = markdown.markdown(md_content)
    
    # 템플릿에 변환된 HTML 내용 전달
    return render(request, 'about.html', {'content': html_content})

def index(request):
    
    ai_objects = AI.objects.all().order_by('-created_at')
    return render(request, "index.html",{'ai_objects': ai_objects})


