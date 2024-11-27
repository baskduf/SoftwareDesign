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
]
