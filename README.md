
# SoftwareDesign 프로젝트

이 프로젝트는 Django 기반 웹 애플리케이션으로, Google의 AI API와 통신하기 위해 환경 변수에 API 키를 설정해야 합니다. 이 문서에는 프로그램을 실행하는 데 필요한 설치 및 설정 절차가 포함되어 있습니다.

## 요구사항

- Python 3.x
- pip (Python 패키지 관리자)

## 설치 방법

### 1. 리포지토리 클론

먼저 프로젝트를 클론하거나 로컬 환경에 다운로드합니다.

```bash
git clone https://github.com/baskduf/SoftwareDesign.git
cd SoftwareDesign
```

### 2. 가상 환경 생성 (선택 사항)

가상 환경을 사용하여 패키지 관리를 독립적으로 설정할 수 있습니다.

```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate      # Windows
```

### 3. 필수 패키지 설치

`requirements.txt` 파일을 이용해 필요한 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

### 4. API 키 발급 및 `.env` 파일 생성

#### API 키 발급
Google의 AI API와 통신하기 위해 API 키가 필요합니다. 다음 링크에서 Google의 API 콘솔에 접속하여 키를 발급받으세요:

- [Google API Console](https://ai.google.dev/)

#### `.env` 파일 생성

프로젝트 루트 디렉터리에 `.env` 파일을 생성하여 환경 변수를 설정해야 합니다. `.env` 파일의 기본 구조는 다음과 같습니다:

```plaintext
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
API_KEY="your_google_api_key_here"
```

> **경로 지정:** `settings.py` 파일에서 `.env` 파일의 경로를 다음과 같이 설정해야 합니다:

```python
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='C:/Users/my/Desktop/SoftwareDesign/.env')
```

### 5. 데이터베이스 마이그레이션

Django 데이터베이스 스키마를 초기화합니다.

```bash
python manage.py migrate
```

### 6. 슈퍼유저 생성 (관리자 계정 생성)

관리자 페이지에 접근하기 위해 슈퍼유저 계정을 생성합니다.

```bash
python manage.py createsuperuser
```

### 7. 개발 서버 실행

개발 서버를 실행하여 애플리케이션을 로컬 환경에서 확인할 수 있습니다.

```bash
python manage.py runserver
```

웹 브라우저에서 `http://127.0.0.1:8000/`에 접속하여 프로젝트를 확인할 수 있습니다.

## 추가 정보

이 프로젝트는 [Django REST Framework](https://www.django-rest-framework.org/), [python-dotenv](https://pypi.org/project/python-dotenv/) 등의 패키지를 사용하여 RESTful API와 환경 변수 관리를 제공합니다.

---

이제 프로그램을 실행할 수 있습니다!
