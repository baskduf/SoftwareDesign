"""
URL configuration for softwaredesign project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views
from django.urls import path, include

urlpatterns = [
    # 기존 URL 패턴
    path('login/', views.login, name='login'),  # 일반 로그인
    path('signup/', views.signup, name='signup'),  # 회원가입
    #path('logout/', LogoutView.as_view(), name='logout'),

    # Google 로그인 관련 URL 패턴
    path('login/google/', views.google_login, name='google_login'),  # Google 로그인 시작
    path('login/google/callback/', views.google_callback, name='google_callback'),  # Google 인증 완료 후 콜백

    # 소셜 로그인 관련 URL 패턴
    path('social/', include('social_django.urls', namespace='social')),  # social_django 기본 URL
]