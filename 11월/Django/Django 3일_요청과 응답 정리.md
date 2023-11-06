# Django 3일_요청과 응답 정리



### 설치, 시작

1. 가상환경을 만들고
   - 설치 (python -m venv) 시작(source ~~) 
2. 가상환경에 장고를 설치하고
   - (pip install django==3.2.13)
3. 프로젝트를 시작한다
   - django-admin startproject 이름 시작경로
4. 프로젝트가 설치된 경로에 앱을 만들자
   - python manage.py startapp 앱이름
   - **설치 후 반드시 settings.py의 INSTALLED_APPS의 첫째줄에 앱을 추가해주자**



### URL, VIEW, TEMPLATE

- urls.py, views.py, template 폴더생성후 페이지를 만들자

#### urls.py

1. 생성한 애플리케이션의 view.py와 연동을 시켜야한다
   - from 어플 import views
     - urlpatterns에 path('경로/<사용자입력>/, views.html파일'), 들을 추가해준다.



#### views.py

1. ```django
   def 경로(request, <사용자입력>):  을 정의해준다.
       딕셔너리 context를 만들어서 관리한다.
       name = ~~
       context = {
       	'name' : name,
      		'img' : '주소',
       }
       ## name을 딕셔너리를 포함한 리스트로 관리해서 이용하면 텍스트, 이미지 모두 뽑아오는게 가능하다.
       name = [
       	{ "name" : "기명", "src" : "a.jpg"}, {"name" : "복길", "src" : "b.jpg"}
       ]
       context = {
       	'name' : name.random.choice(),
       }
       이러고, html 파일에서 {{ name.name }} / {{ name.src }} 이런식으로 사용이 가능함(연동됨)
       return render(request, '경로.html', context)
   ```



#### template

1. template 폴더를 애플리케이션 폴더 내부에 만들어서, 그 안에 html파일들을 만들어 관리한다.
   - **Django 특유의 {{ 변수 }}, {% for i in ~~ %} {% endfor %} 등의 문법을 이용하자.**