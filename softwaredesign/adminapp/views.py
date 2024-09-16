from django.shortcuts import render
from .forms import createAIForm
# Create your views here.

def index(request):
    return render(request, "admin-index.html")

# myapp/views.py
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import createAIForm

def create(request):
    if request.method == 'POST':
        form = createAIForm(request.POST, request.FILES)
        if form.is_valid():
            # 폼 데이터 처리
            ainame = form.cleaned_data['ainame']
            prompt = form.cleaned_data['prompt']
            image = form.cleaned_data['image']

            # 이미지 파일 저장
            if image:
                file_path = default_storage.save(f'images/{image.name}', ContentFile(image.read()))
                # 파일 저장 경로를 사용하여 추가 작업을 수행할 수 있습니다.
                print(f'Image saved to: {file_path}')

            # 데이터 저장 또는 다른 처리를 수행
            # 예를 들어, 데이터베이스에 저장하거나 다른 API 호출 등을 할 수 있습니다.
            # ...

            return redirect('success')  # 성공 페이지로 리다이렉트
    else:
        form = createAIForm()

    return render(request, 'admin-create.html', {'form': form})
