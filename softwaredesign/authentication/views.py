from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
<<<<<<< HEAD
from softwaredesign import settings
from django.contrib.sites import requests
=======
from django.contrib.auth import logout

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth

def social_login(request):
    if request.user.is_authenticated:
        # 카카오 로그인 후, 사용자의 정보 가져오기
        kakao_user_info = request.user.social_auth.get(provider='kakao').extra_data
        email = kakao_user_info.get('kakao_account', {}).get('email')
        name = kakao_user_info.get('properties', {}).get('nickname')
        
        # 기존 사용자가 존재하는지 확인
        if not User.objects.filter(email=email).exists():
            # 신규 사용자일 경우 회원가입 진행
            user = User.objects.create_user(username=email, email=email, password=None)
            user.first_name = name  # 이름 설정
            user.save()

            # 회원가입 후 로그인
            login(request, user)
        
        # 기존 사용자라면 바로 로그인
        else:
            user = User.objects.get(email=email)
            login(request, user)

        return redirect('/')  # 로그인 후 리다이렉트

    return redirect('social:begin', 'kakao')  # 로그인 페이지로 리다이렉트


def out(request):
    logout(request)
    return redirect('/')  # 로그아웃 후 리디렉션할 URL

>>>>>>> main
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

# Google 로그인 시작 뷰
def google_login(request):
    """
    Google OAuth2 로그인 요청
    """
    google_auth_endpoint = 'https://accounts.google.com/o/oauth2/v2/auth'
    redirect_uri = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI
    scope = 'openid email profile'
    response_type = 'code'

    client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY

    auth_url = (
        f"{google_auth_endpoint}?response_type={response_type}&client_id={client_id}"
        f"&redirect_uri={redirect_uri}&scope={scope}"
    )

    return redirect(auth_url)

# Google 로그인 콜백 뷰
def google_callback(request):
    """
    Google 인증 후 사용자 처리
    """
    code = request.GET.get('code')
    if not code:
        messages.error(request, 'Authentication failed. No code provided.')
        return redirect('/auth/login/')

    # Access Token 요청
    token_url = 'https://oauth2.googleapis.com/token'
    redirect_uri = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI
    client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    client_secret = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

    token_data = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }

    token_response = requests.post(token_url, data=token_data)
    token_json = token_response.json()
    access_token = token_json.get('access_token')

    if not access_token:
        messages.error(request, 'Failed to obtain access token.')
        return redirect('/auth/login/')

    # Google 사용자 정보 요청
    user_info_url = 'https://www.googleapis.com/oauth2/v3/userinfo'
    user_info_response = requests.get(
        user_info_url, headers={'Authorization': f'Bearer {access_token}'}
    )
    user_info = user_info_response.json()

    email = user_info.get('email')
    name = user_info.get('name')

    if not email:
        messages.error(request, 'Failed to retrieve email address.')
        return redirect('/auth/login/')

    # 사용자 생성 또는 가져오기
    user, created = User.objects.get_or_create(username=email, defaults={'email': email, 'first_name': name})
    if created:
        user.set_unusable_password()
        user.save()

    # 로그인 처리
    auth_login(request, user)
    messages.success(request, 'You have successfully logged in with Google!')
    return redirect('/')