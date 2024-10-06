# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # 커스텀 필드를 관리 페이지에서 보여주기 위해 추가
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('ainame',)}),  # 튜플로 정의
)

admin.site.register(User, CustomUserAdmin)
