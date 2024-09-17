from django.shortcuts import render, get_object_or_404

from .models import AI

def index(request, ainame):
    ai = get_object_or_404(AI, ainame=ainame)
    image_url = ai.get_image_url()  # 이미지 경로 생성

    return render(request, 'ai-index.html', {
        'ai': ai,
        'image_url': image_url  # 이미지 경로 템플릿에 전달
    })

def chat(request, ainame):
    ai = get_object_or_404(AI, ainame=ainame)
    image_url = ai.get_image_url()  # 이미지 경로 생성

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

# .env 파일 로드
load_dotenv(dotenv_path='C:/Users/my/Desktop/SoftwareDesign/.env')

# 환경 변수에서 API 키 가져오기
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY is not set in the environment variables.")

# Gemini API 클라이언트 설정
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_prompt_text():
    # 파일 경로를 지정 (프로젝트의 static 디렉터리 내)
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


def chat_api_request(request,message, ainame):
    try:
        
        ai_object = AI.objects.get(ainame=ainame)

        prompt = get_prompt_text()
        prompt = replace_placeholders(prompt, ai_object.personality, 0, ainame, message)

        result = model.generate_content(prompt)
        return {'result': result.text}
    except Exception as e:
        return {'error': str(e)}

@csrf_exempt
def chat_api_view(request, ainame):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)


            message = data.get('message')
            response = chat_api_request(request=request, message=message, ainame=ainame)
            return JsonResponse(response)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
