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
from . import views

urlpatterns = [
    
    path('api/<str:ainame>/', views.chat_api_view, name='chat_api'),
    path('<str:ainame>/', views.index, name='ai_index'),
    path('<str:ainame>/chat/', views.chat, name='ai_chat'),
    
    path('<str:ainame>/recommend/', views.recommend_ai, name='recommend_ai'),
    
    path('<str:ainame>/subscribe/', views.subscribe, name='subscribe'),
    path('<str:ainame>/unsubscribe/', views.unsubscribe, name='unsubscribe'),

    path('<str:ainame>/Review_View/', views.Review_View, name='Review_View'),  # AI 세부 페이지 URL
    path('<str:ainame>/Review_Create/', views.Review_Create, name='Review_Create'),  # 리뷰 작성 페이지 URL
    path('<str:ainame>/Review_Edit/<int:review_id>/', views.Review_Edit, name='Review_Edit'),  # 리뷰 수정 URL
    path('<str:ainame>/Review_Delete/<int:review_id>/', views.Review_Delete, name='Review_Delete'),  # 리뷰 삭제 URL
]
