from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, LoginForm
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

from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # 사용자 인증
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                # 로그인 처리
                auth_login(request, user)
                messages.success(request, 'You are now logged in!')
                return redirect('/')  # 로그인 후 리다이렉트할 페이지를 설정합니다.
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})