# App URL mapping

- 앱이 여러개가 되면 url을 project의 urls.py에서 관리하기



- 당장 실라버스, 유튜브 등도 다양한 어플들이 존재함.



### Namespace

- 앱별로 제공하며, 앱마다 다른 이름공간을 가지도록..
- 개체를 구분할 수 있는 범위를 나타내는 이름공간.



- 예를들어 앱이 둘이상 있을때, 
  - pages/templates/index.html
  - articles/templates/index.html 이라는 각각다른앱의 index.html에서
    - articles의 urls.py에서, path()의 3번째 요소에 name='index' 같은걸 넣어줘야함.
    - 이렇게 하면, articles의 템플릿들에 index라는 이름을 넣어주면 url을 넣을수있음.
      - a href="{% url 'index' %}" 이런 a태그 가능
        - (DTL url 문법?)



### URL Namespace

- 서로 다른앱에서 동일한 url이름을 사용해도 지정된 url을 고유하게 사용할수있음
- app_name attribute를 작성해 URL namespace를 설정
  - articles/urls.py에서,
    - app_name = 'articles'
    - urlpatterns = [ ... ]
  - pages/urls.py에도
    - app_name = 'pages'
- 이렇게 하고난 다음에, { % url'create' %} 같은걸 { % url'articles:create' %} 로 바꿔야 인식함 (url태그들)