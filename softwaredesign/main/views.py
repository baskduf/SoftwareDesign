from django.shortcuts import render
from dotenv import load_dotenv
import os

# .env 파일의 경로를 명시적으로 지정
load_dotenv(dotenv_path='C:/Users/my/Desktop/SoftwareDesign/.env')

# 환경 변수에서 API 키 가져오기
api_key = os.getenv('API_KEY')


# Create your views here.
def index(request):
    return render(request, "index.html")


