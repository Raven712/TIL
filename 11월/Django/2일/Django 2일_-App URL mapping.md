# Django 2일_-App URL mapping



### Namespace

- path('index/', views.index, name='index') 
  - name='index' 라는걸 붙여줬다.
  - 템플릿 파일(html)에 돌아가서, href 같은 속성에 넣어줄수가 있음.
    - a href="{% url 'index' %}"
    - form action="{% url 'create' %}"

- 저걸 해주면 뭐가 좋나? (변수화)
  -  url이 바뀔때 재사용성이 올라감
  - 하지만 index같이 이름이 다른앱에서도 중복이 되는 상황이 생기면 문제가 생김
    -  (app1, 2의 index name을 전부 index로 하면)



### URL Namespace

- 위의 문제를 해결하기 위함

- 각각의 앱의 urls.py에서 app_name attribute를 작성해 URL namespace 설정

  ```django
  app_name = 'app_1'
  urlpatterns = [path(~~) name='index']
  ```

- URL 태그는 {% url 'app_1:index' %} 로 바꿔 주어야함.



### Template Namespace

- 이건 어제 했던 Templates 폴더 내부에 앱이름과 같은 폴더를 만든 내용임.
- 다중 앱 프로젝트에서 html 파일 이름이 동일한게 있을때 생길 문제를 예방하기 위한것



## 마무리

장고의 설계 철학

1. 표현, 로직(view)을 분리
   - 템플릿 시스템은 표현을 제어하는 도구, 표현에 관련된 로직
   - 이 기본목표를 넘어서는 기능 지원 하지말아야함
2. 중복 배제
   - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 디자인을 가짐
   - 장고 템플릿 시스템은 이런 요소를 한곳에 저장하기 쉽게 해서 중복코드 없애줘야함
   - 템플릿 상속의 기초가 되는 철학



프레임워크의 성격

- 독선적(Opinionated)
  - 어떤 특정 작업을 다루는 올바른 방법에 대한 분명한 규약이 있음.
  - 그게 문서화가 잘 돼있음

- 관용적(Unopinionated)
  - 구성요소를 한데 붙여서 해결해야하거나 어떤 도구를 써야한다 같은 제약이 별로 없음
  - 근데 문제해결도구를 개발자가 직접 찾아야됨

- 장고는 다소 독선적