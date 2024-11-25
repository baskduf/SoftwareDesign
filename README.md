
# ✨ SoftwareDesign 프로젝트 🌍

> **Django로 만들어진 AI 애플리케이션, 시작부터 끝까지 함께 해보세요!**

---

## 💡 필수 준비물

- 🐍 Python 3.x (최신 버전으로 준비 완료!)
- 📦 pip (Python의 든든한 친구)

---

## 🎉 따라 하기! 설치 방법

### 🌱 1단계: 프로젝트 가져오기

먼저 리포지토리를 클론합니다.

```bash
git clone https://github.com/baskduf/SoftwareDesign.git
cd SoftwareDesign
```

---

### 🧪 2단계: 나만의 가상 환경 만들기 (선택사항)

> 프로젝트 별로 가상 환경을 쓰면 설치된 패키지가 깔끔하게 관리됩니다!

```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate      # Windows
```

---

### 📦 3단계: 패키지 설치 – 준비 완료!

> `requirements.txt`로 모든 필수 패키지를 한번에 설치할 수 있어요. 간단하죠?

```bash
pip install -r requirements.txt
```

---

### 🔑 4단계: API 키 생성 및 `.env` 파일 설정

#### 🌐 Google AI API 키 발급받기
Google의 AI API와 통신하기 위해 **API 키**가 필요해요. 아래 링크에서 발급받아 보세요:
- [🔗 Google API Console](https://ai.google.dev/)

#### 📂 `.env` 파일 생성하기
프로젝트 루트에 `.env` 파일을 만들고 아래처럼 **API_KEY** 값을 입력해 주세요:

```plaintext
API_KEY="your_google_api_key_here"
```

> **TIP:** 경로는 `aiservice/views.py` 파일에서 이렇게 지정하면 됩니다:

```python
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='C:/Users/my/Desktop/SoftwareDesign/.env')
```

---

### 📊 5단계: 데이터베이스 마이그레이션

```bash
python manage.py migrate
```

> **다 했으면...** 이제 데이터베이스가 준비되었습니다! 

---

### 🔓 6단계: 슈퍼유저 만들기

관리자 페이지에서 자유롭게 설정할 수 있도록 **슈퍼유저 계정**을 만들어 보세요!

```bash
python manage.py createsuperuser
```

---

### 🚀 7단계: 개발 서버 시작하기

드디어! 서버를 실행하고 로컬 환경에서 웹 애플리케이션을 확인해 볼 시간입니다.

```bash
python manage.py runserver
```

이제 웹 브라우저에서 🌍 `http://localhost:8000/`에 접속해 보세요!

---

## 🧠 프로그램 설명

### 프로그램 주요 기능
이 프로그램은 **AI와 사용자 간의 상호작용을 중심으로 한 Django 기반의 애플리케이션**입니다.  
다음은 주요 기능입니다:

1. **관리자 기능**:
   - 여러 AI의 프롬프트를 생성하고 관리할 수 있습니다.
   - AI의 성격, 답변 스타일 등을 설정하여 각 AI를 개별적으로 정의할 수 있습니다.

2. **사용자-AI 채팅**:
   - 사용자는 다양한 AI와 채팅할 수 있습니다.
   - AI와의 대화 내용은 **채팅 로그**로 기록됩니다.

3. **호감도 관리**:
   - 사용자는 각 AI와의 상호작용을 통해 **호감도**를 쌓을 수 있습니다.
   - 호감도는 데이터베이스에 저장되어, AI의 응답 스타일에 영향을 줄 수 있습니다.

### 데이터베이스 구성
- **AI 모델**: 각 AI의 이름, 성격, 프롬프트 등이 저장됩니다.
- **사용자**: 사용자 정보 및 AI와의 상호작용 기록이 저장됩니다.
- **채팅 로그**: 사용자와 AI 간의 대화 내용이 기록됩니다.
- **호감도**: AI와 사용자 간의 관계 상태를 나타내며, 채팅 로그와 연결됩니다.

---

## 🌈 알아두면 좋은 정보

이 프로젝트는 **Django REST Framework**와 **python-dotenv** 패키지를 사용해 RESTful API와 환경 변수 관리를 쉽게 해줍니다. 더욱 편리하고 깔끔하게 코딩할 수 있어요!

---

이제 준비가 모두 끝났습니다! 😄 **환영합니다, SoftwareDesign 프로젝트에 오신 것을!**
