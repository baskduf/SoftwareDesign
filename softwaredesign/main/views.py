from django.shortcuts import render
from dotenv import load_dotenv
import os

# .env 파일의 경로를 명시적으로 지정
load_dotenv(dotenv_path='C:/Users/my/Desktop/SoftwareDesign/.env')

# 환경 변수에서 API 키 가져오기
api_key = os.getenv('API_KEY')


# Create your views here.
def index(request):
    return render(request, "index.html")


# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=email, email=email, password=password)
                messages.success(request, 'Thank you! Your submission has been received!')
                return redirect('/')  # 성공 시 리다이렉트할 페이지를 설정합니다.
            else:
                messages.error(request, 'Oops! Something went wrong while submitting the form.')
        else:
            messages.error(request, 'Oops! Something went wrong while submitting the form.')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})
