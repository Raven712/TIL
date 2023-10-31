# Django 3일_Variable Routing

- URL 주소를 변수로 사용하는 것
- URL 일부를 변수로 지정해서 view 함수의 인자로 넘기기 가능
- 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음



### 작성

- 변수를 <> 에 정의
  - path('index/<name>/', views.index),
- views.py에서
  - def index(request, name): ~~
- html 파일에서(템플릿)
  - {{ name }} 이런식으로 변수로 사용가능



## Form 태그 - client

- html의 form 태그.
- 데이터가 전송되는 방법을 정의
- 웹에서 사용자 정보를 입력하는 여러방식(text, submit, button 등)제공,
  - 사용자로부터 할당된 데이터를 서버로 전송하는 역할 담당.
- 데이터를 어디(action)로 어떤 방식(method)으로 보낼지.
  - method="GET"에서, GET을 보면
    - 데이터의 딕셔너리가 나오는데, 그 키 값이 



- http://search.naver.com/serach.naver?query=롤드컵
  - form의 action에 정의한 내용
    - http://search.naver.com/serach.naver
  - query=롤드컵
    - input으로 정의한 데이터



- input 태그의 name을 활용해서 views의 인자 request를 활용하기가 가능해짐
  - input type = "text" name="ball" 해두고
  - views에서 name = request.GET.get('ball') 같은걸 해줄수가 있음

