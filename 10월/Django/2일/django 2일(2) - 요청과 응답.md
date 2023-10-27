# django 2일(2) - 요청과 응답

- 웹을 통한 요청은 URL을 통해,
- 응답은 문서 (HTML)로 받는것.



- URL -> VIEW -> Template 순의 작성 순서로 코드작성, 데이터 흐름 이해하기
  - 1. 주문서 정의 ---> URL (urls.py에 담기)
    2. 로직 구현 ---> views.py
    3. HTML 페이지 구성 ---> template (html파일들)



## urls.py

- 첫번쨰 페이지 (홈페이지) 를 index로 표현을 자주함
- urlpatterns에 path('index/', 어떤 view 파일의 어떤 함수에서 핸들링 할지) 를 적어주자.
  - 여기선 path('index/', views.index), 로 해서, views.py의 index함수로 핸들링 하겠다고 적어주자.
  - 그리고 views.py는 만든 애플리케이션 안에 있는 파일이라, import를 해줘야함.
  - from (애플리케이션명) import views

***

- template에서 돌아왔다면, path를 추가해보자.
  - path('welcome/<name>/', views.welcome)

## views.py

- urls.py의 두번째 줄에 따라, views.py로 가자.

  - views.py의 index 함수로 핸들링 한댔으니 함수를 만들면 된다.

  - ```python
    def index(request):
        # 환영하는 메인페이지를 보여주자.
        # index() 내부엔 요청에 대한 정보, request를 첫째 파라미터로 넣어준다
        name = random.choice(['기명', '복길', '기훈', '멍멍'])
        ## 여기서 na
        
        context = {
            'name' : name,      # 이런식으로 딕셔너리에 값을 변수로 넣어줄수도 있다.
            'img' : 'https://thumb.mt.co.kr/06/2023/02/2023020119382519378_1.jpg/dims/optimize/'
        }
        return render(request, 'index.html', context)
    # 무언가를 만들면서(render) 끝낸다.
    # 그 무언가는 index.html 파일이고, 이건 나중에 만들어서 보내주는것..
    # render의 첫번쨰 인자로 request를 넣는건 일종의 django 약속!
    # context는 선택인자. (딕셔너리에서 사용할 데이터)
    
    # context를 통해서 html파일을 동적으로 만들어줄수 있음.
    ```
    
    



## template

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의
- Template 파일의 기본 경로
  - app 폴더 안의 templates 폴더



- 지금은 templates 폴더를 생성해서, 그 안에 index.html을 만들어주고 작성하면됨.

  - 이 html파일은 django로 인해 동적 페이지로 만들수있음.

  - ```django
    <h1>
        {{ name }}님 환영합니다 # name은 views.py의 index함수 내부의 name
        # 그런데 이 name을 사용자의 입력에 따라 달라지게 하려면? (Variable Routing)
        # 주문서인 urls.py로 다시 돌아가자
    </h1>
    
    # {{ }} << 얘를 mustach 기호라고 함.
    # {{ }} 안에 들어갈 수 있는 변수는, views.py의 context 딕셔너리에 등록해놓은 key.
    
    # 예를들어 views.py context에 {}
    ```
    
  - 