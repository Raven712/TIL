# django 2일(1)



### 명령어들

- source 경로/Scripts/activate
  - 가상환경 켜키

- django-admin startproject 프로젝트이름 시작경로
  - 프로젝트시작
- python manage.py runserver
  - 서버 돌리기

- rm -r (지울 가상환경 이름)
  - 가상환경 지우기

- python manage.py startapp 이름
  - 어플리케이션 생성



### 프로젝트 구조

- init.py
  - 디렉토리를 파이썬 패키지로 다루도록 지시, 안건드림
- asgi.py
  - Django 어플리케이션 비동기식 웹서버와 연결, 소통 도움 
  - 배포시 사용
- settings.py
  - 세팅들
- urls.py
  - 사이트의 url, views의 연결 지정
- wsgi.py
  - 얘도 배포시 사용
- manage.py
  - Django 프로젝트와 다양한 방법으로 상호작용하게하는 커맨드라인 유틸리티



### 애플리케이션 구조

- admin.py

  - 관리자용 페이지 설정하는 곳

- 앱을 사용하려면 Installed_Apps에 등록해야됨

  - 프로젝트 폴더의 settings.py에 있음!

    