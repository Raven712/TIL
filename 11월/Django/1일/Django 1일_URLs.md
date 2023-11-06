# Django 1일_URLs



- URL의 경로가 겹치면? (app1의 view와 app2의 view가 중복이 생기면)

  - from app1 import views as app1_views

    - 이런식으로 as를 사용하는 방법이 있다.

  - 근데 만약 app1에도 index.html, 2에도 index.html이 있으면?

    - 2의 index가 열린다?
    - **templates 폴더가 여러개의 앱에 있지만, django는 하나의 폴더로 인식을 해버림**
    - 왜그렇냐면 settings.py에 앱등록 순서가 2가 먼저돼있어서 그럼
    - **그래서 그냥쓰면 템플릿 상속같은게 자유로움**

    - 아무튼 이 특성때문에 생긴 **컨벤션**은 -

      - templates 폴더 내부에 앱이름과 같은 폴더를 만들어서 그 안에 html파일을 넣어서 씀.
      - 그리고 views의 render를 render(request, 'app1/index.html')
      - 이런식으로 경로를 따로 지정해줌.
      - templates 폴더내부에 app1 app2 폴더를 따로만들어서 관리한다고 생각하면 된다.

      

  - base.html을 참고하려면 (extends)?

    - extends는 최상단을 기준으로 참고하므로, 앱이아닌 프로젝트 폴더에 templates 폴더를 만들어서,
      - 그 안에 base.html을 넣고 (아무튼 중립, 상단영역으로 템플릿폴더를 옮겨오는것)
    - settings.py의 TEMPLATES의 DIRS에 해당 폴더를 추가해서 사용하는게 **컨벤션**이다 
      - DIR = [BASE_DIR / 'templates']
      - 프로젝트의 최상단 영역 (BASE_DIR) 의 templates 폴더를 templates로 참조하겠다는 의미.