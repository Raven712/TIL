# 장고 복습-5 (요청과 응답, url~templates)

웹 서비스는 요청과 응답이라는 형식으로 진행됨.



브라우저를 통해 URL로 요청, 문서(HTML)를 통해 응답하는게 기본.



1. 클라이언트의 주문서를 정의하고 (URL 정의. urls.py 파일 관리)
2. 어떻게 정보를 취득하여 만들어줄지 (처리 로직 구현. views.py파일 관리)
3. 서버가 정보를 html 페이지에 담아 보여주는 것(template. index.html 따위)

**URL -> View -> Template 순의 작성 순서로 코드 작성, 데이터 흐름 이해하기.**

**물론 가장먼저 settings.py의 Installed_apps에 앱을 등록해야 작동한다.**



### URL(urls.py)

- urlpatterns = [ ~~~ ] 리스트를 조절하자.

  - path('index/'(주문서), 어떤 view 파일의 어떤 함수에서 핸들링 할것인지 ) 를 추가한다면,
    - ex) path('index/', views.index),
  - urls.py의 index라는 주소를 view파일의 특정함수가 핸들링 하게되는것.
    - 물론 여기에서의 view가 무엇인지 알게하려면, from 앱이름(여기선 articles) import views를 해줘야 인식을 하게됨.
    - ex) from articles import views

- 기타 응용은 views의 하단에서 참고!

  

### View(views.py)

- 위처럼 했으니, ariticles 앱의 views.py로 가서, index를 만들어줘야함.

  - def index(request(요청한 무언가의 정보), ):

    - return render(request(요청자), 'index.html'(템플릿 이름), context)

      - context는 딕셔너리 데이터. 이걸 템플릿에 전달해줌.
      - 그리고 context는 def index함수 안에 딕셔너리를 넣어주는식.
      - ex) context = { 'name' : '기명', 'img' : 'www.~~~',} 이런식으로..
        - **이렇게하면 템플릿에 --> name, 환영합니다 이런게 가능하게됨!**
        - **template에 {{ 변수명 }}, 여기선 name을 넣어주면됨.** 머스태쉬 태그.
        - 주소는 따옴표는 유지시켜야함. 
        - ex) <img src="{{ img }}" 이런식

    - 응용하면 def index 함수안에, 리스트를 추가할수도 있음. 그리고 random 모듈을 불러와서 choice() 함수를 쓰거나.. 그럴수도 있음

      - import random
      - ex) names = ['복길', '복돌', '복실']
      - name = random.choice(names)
      - 그리고 context의 name을 name으로 등록시키면?
        - 사이트 들어갈때마다 이름이 랜덤으로 나옴.

    - 더 응용하면 클라이언트가 주문서에 적는 이름에 따라 환영메시지가 바뀌게 할 수도 있음.

      - 이건 urls.py에서 고치면 됨

      - **path('welcome/<name/', views.welcome) <> <<< 얘가 변수로 처리한다는 의미! **, 그리고 welcome이라는 함수를 추가로 만들어서 다룬다는것.

      - 다시 views.py에서 **def welcome(request, name)**을 해주고, 여기서 다시 return을 welcome.html로 해서, 새로운 html 파일을 만들고, 

        - 주문서에 들어온 이름에 따라 이름이 출력되도록 바꿔주자. {{}} 를 이용해서.

      - **context 딕셔너리의 내용물을 리스트로 등록시킬 수도 있음!!**

        - ex) context = { 'names' : ['복길', '복실']}  해놓고

        - template 파일(welcome.html)에서,

        - ```python
          {% for name in names %}
          	{{ name }}
          {% endfor %}
          ```

          위처럼 해주면 된다.

          <p {{name}} </p 를 해주면 br이 적용되어서 여러줄로 나옴!

    - 예를들어 환영 메인페이지를 보여주는거라면. index.html을 환영메인페이지로 만들자.(템플릿)

      

### Templates

- 실제 내용을 보여주는데 사용되는 파일
- 파일의 구조나 레이아웃을 정의.
- 템플릿 파일의 기본경로 : app 폴더 안의 templates 폴더. (폴더를 만들어야됨)
  - app_name/templates/