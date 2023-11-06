# Django 1일_URLs(2)



### App URL mapping

- 앱이 많아졌을때 urls.py를 각 앱에 매핑하는 법
- app의 view함수가 많아지면서 path도 많아지고 해서 프로젝트의 urls.py에서 모두 관리하는건
  -  프로젝트의 urls.py에서 모두 관리하는건 유지보수에 좋지않음
  - view 함수를 import 할떄 as를 붙이는 방법도 있지만. 역시 좋지않음



- 각각의 앱 안에 urls.py를 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁하자

  - 각 앱의 urls.py를 만들고 대충 본인앱의 path들같은걸 만들어준 뒤 
  - 다시 프로젝트의 urls.py로 돌아와서,
    - from django.urls import path, **include** 를 넣어주고
    - path('app_1/', include('app_1.urls')), 이걸 넣어준다.
      - 만약 루트페이지로 app_1을 설정하고싶으면 path(''/, include('app_1.urls'))
      - 위의 path문은 localhost:8000/app_1/~~~ 을 하겠다는 의미니까
    - include는 앞으로는 app_1에 대한건 app_1.urls에 넘기겠다는 의미

  

  