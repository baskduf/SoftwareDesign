from django.contrib import admin
from django.urls import path
from start import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('board/', views.board_list, name='board_list'),
    path('board/create/', views.create_post, name='create_post'),
    path('', views.home, name='home'),  # 홈 페이지를 로그인 페이지로 렌더링
]
