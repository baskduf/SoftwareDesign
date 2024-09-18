from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json
from start.models import Post

def home(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'message': 'Logged in successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success', 'message': 'Logged out successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def board_list(request):
    if request.method == 'GET':
        posts = Post.objects.all().values('title', 'content', 'author__username', 'created_at')
        return JsonResponse(list(posts), safe=False)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            content = data.get('content')
            if request.user.is_authenticated:
                Post.objects.create(title=title, content=content, author=request.user)
                return JsonResponse({'status': 'success', 'message': 'Post created successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
