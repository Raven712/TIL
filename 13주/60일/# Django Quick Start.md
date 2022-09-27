# Django Quick Start

server 폴더내부, firstpjt 내부에 들어가보면 파일들이 있는데.

- _ _ init _ _.py
  - 그냥 이런게 있음.. (건드릴일이 없음)
- asgi.py 
  - Asynchronous Server Gateway Interface
    - 비동기식 웹서버연결-소통 도움
    - 배포시에 사용하며 지금은 수정하지않음
- settings.py
  - 장고 프로젝트 설정을 관리
- urls.py
  - 사이트의 url, 적절한 view의 연결을 지정
- wsgi.py
  - Web Server Gateway Interface
  - 얘도 잘안씀..?
- manage.py
  - 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
  - ex) $ python manage.py 명령어 설정
    - $ python manage.py startapp 앱이름 (이름은 복수형이 권장됨)
      - 앱 생성
      - 이렇게하면 폴더가 생성됨. 폴더내부에 views.py가 중요하다.. ?



***

가상환경 실행하기. (안하면 전부다 안됨)

- server-venv 안에 Scripts 안에 activate라는 파일이 있음. 이걸 실행해야함.

- $ source [server-venv]/Scripts/activate

  - 우리는 이미 장고를 가상환경안에 설치해놨음. 여기서 돌려야됨
  - global 환경에도 장고가 있을수도있음.

  

***

앱 생성후 추가..? 

- firstpjt/settings.py 를 vscode로 켜면 파이선 코드가 있음.
- Installed_apps = [ ~~~ ] 라는 리스트가 있음.
  - 여기 리스트 요소중 최상단에 우리가 만든 'articles' 를 넣어주면 됨.



앱을 지우려면?

- Installed_apps 에서 앱을 지움.
- 그냥 articles 폴더 지우면 됨.



***

프로젝트와 앱?

- 프로젝트는 앱의 집합.
- 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당.
- 일반적으로 앱은 하나의 역할-기능단위로 작성되는게 권장됨.