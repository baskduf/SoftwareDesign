from django.shortcuts import render, get_object_or_404

from .models import AI
from authentication.models import UserAI

def index(request, ainame):
    if not request.user.is_authenticated:
        return redirect('login')  # 로그인 페이지로 리다이렉트하거나 오류 페이지로 이동
    
    ai = get_object_or_404(AI, ainame=ainame)
    image_url = ai.get_image_url()  # 이미지 경로 생성
    userai = get_or_create_user_ai(request, ai_name=ainame)

    return render(request, 'ai-index.html', {
        'ai': ai,
        'userai':userai,
        'image_url': image_url  # 이미지 경로 템플릿에 전달
    })


from django.contrib.auth import authenticate
from django.shortcuts import redirect
from authentication.models import User
from aiservice.models import AI

def add_ai_to_user(user, ai):
    # 사용자가 AI를 보유하고 있는지 확인
    if not user.ainame.filter(id=ai.id).exists():
        # AI 추가
        user.ainame.add(ai)
        print(f"{user.username}/ {ai.ainame} add")

def chat(request, ainame):
    if not request.user.is_authenticated:
        return redirect("/auth/login/")
    
    ai = get_object_or_404(AI, ainame=ainame)
    image_url = ai.get_image_url()  # 이미지 경로 생성
    user = User.objects.get(username=request.user.username)  # 사용자 가져오기

    add_ai_to_user(user, ai)

    return render(request, 'ai-chat.html', {
        'ai': ai,
        'image_url': image_url  # 이미지 경로 템플릿에 전달
    })

from dotenv import load_dotenv
import os
import json
import requests
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from aiservice.models import AI
from authentication.models import UserAI

import os
from dotenv import load_dotenv

# 프로젝트 최상단 경로 동적으로 계산
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# .env 파일 경로 설정
dotenv_path = os.path.join(project_root, '.env')

# .env 파일 로드
load_dotenv(dotenv_path=dotenv_path)
# 환경 변수에서 API 키 가져오기

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY is not set in the environment variables.")

# Gemini API 클라이언트 설정
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_prompt_text(ai_object):
    # 파일 경로를 지정 (프로젝트의 static 디렉터리 내)
    # AI 객체가 제공되면 AI 객체의 prompt를 우선 사용

    if ai_object and ai_object.prompt:         
        return ai_object.prompt
    
    prompt_file_path = os.path.join('static', 'prompt', 'prompt.txt')

    try:
        # 파일을 열고 내용을 문자열로 읽어서 반환
        with open(prompt_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."

def replace_placeholders(content, 성격, 호감도, 이름, 질문):
    # 문자열 내 플레이스홀더를 각각의 값으로 대체
    content = content.replace("{성격}", 성격)
    content = content.replace("{호감도}", str(호감도))
    content = content.replace("{이름}", 이름)
    content = content.replace("{질문}", 질문)
    return content

from authentication.models import ChatLog

def add_chat_log(user, ai, message):
    # 새로운 ChatLog 인스턴스 생성
    
    add_ai_to_user(user, ai)

    chat_log = ChatLog(user=user, ai=ai, message=message)
    chat_log.save()  # 데이터베이스에 저장
    print(f"채팅 로그가 추가되었습니다: {message} (User: {user.username}, AI: {ai.ainame})")

def chat_with_ai(request, ai_name):
    ai = AI.objects.get(ainame=ai_name)
    
    # 최근 30개의 채팅 로그 가져오기
    chat_logs = ChatLog.objects.filter(user=request.user, ai=ai).order_by('-timestamp')[:30]

    # 채팅 로그를 문자열로 변환
    if chat_logs.exists():
        chat_log_str = '\n'.join([f"사용자: {log.message} ({log.timestamp})" for log in chat_logs[::-1]])
    else:
        chat_log_str = "채팅 로그가 없습니다."

    if request.method == 'POST':
        user_message = request.POST.get('message')  # 사용자의 메시지
        if user_message:  # 메시지가 비어 있지 않은 경우에만 저장
            add_chat_log(request.user, ai, user_message)  # 채팅 로그 추가

    # 문자열 반환
    return chat_log_str

def get_or_create_user_ai(request, ai_name):
    ai = AI.objects.get(ainame=ai_name)

    user_ai, created = UserAI.objects.get_or_create(
        user=request.user,
        ai=ai,
        defaults={'affection': 0}  # 없을 경우 affection을 0으로 설정
    )

    if created:
        print("새로운 UserAI가 생성되었습니다.")
    else:
        print("기존 UserAI를 찾았습니다. affection:", user_ai.affection)

    return user_ai  # affection 값 반환


def chat_api_request(request,message, ainame):
    try:
        
        user_ai = get_or_create_user_ai(request, ai_name=ainame)

        ai_object = AI.objects.get(ainame=ainame)
        check_prompt = (
            f"#질문 을 듣고 이 단어가 호감에 대한 단어인지 아닌지 파악하고 반드시 (yes/no)로만 대답해줘\n"
            f"#질문: {message}"
        )

        result = model.generate_content(check_prompt)

        if result.text.strip().lower() == "yes":
            user_ai.affection += 1  # affection 증가
            user_ai.save()  # 업데이트된 affection을 데이터베이스에 저장

        prompt = get_prompt_text(ai_object)
        prompt = replace_placeholders(prompt, ai_object.personality, 0, ainame, message)
        prompt.replace("{채팅로그}", chat_with_ai(request, ainame))
        print(prompt)
        result = model.generate_content(prompt)
        

        return {'result': result.text, 'affection': user_ai.affection}
    except Exception as e:
        return {'error': str(e)}
    

@csrf_exempt
def chat_api_view(request, ainame):
    if request.method == 'POST':
        try:
            
            ai_object = AI.objects.get(ainame=ainame)
            data = json.loads(request.body)


            message = data.get('message')
            response = chat_api_request(request=request, message=message, ainame=ainame)
            

            add_chat_log(request.user, ai_object, response)
            return JsonResponse(response)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

def recommend_ai(request, ainame):
    ai = get_object_or_404(AI, ainame=ainame)
    ai.recommend()  # 추천 횟수 증가
    return redirect(reverse('ai_index', args=[ainame]))


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AI

@login_required
def subscribe(request, ainame):
    ai = get_object_or_404(AI, ainame=ainame)
    
    user_ai = get_or_create_user_ai(request, ai_name=ainame)
    user_ai.subscribe()
    return redirect(reverse('ai_index', args=[ainame]))  # 구독 후 이동할 페이지

@login_required
def unsubscribe(request, ainame):
    ai = get_object_or_404(AI, ainame=ainame)
    user_ai = get_or_create_user_ai(request, ai_name=ainame)
    user_ai.unsubscribe()
    return redirect(reverse('ai_index', args=[ainame]))  # 구독 후 이동할 페이지

