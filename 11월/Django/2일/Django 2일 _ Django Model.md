# Django 2일 _ Django Model

- DB
  - 체계화된 데이터의 모임
  - 검색-구조화같은 작업 위해 조직화된 데이터를 수집하는 저장 시스템

- 기본 구조
  - 스키마
    - 메타데이터 (id INT, name TEXT...)
    - 데이터베이스의 자료구조, 표현방법, 관계등을 정의한 구조
  - 테이블
    - 필드와 레코드를 사용해 조직된 데이터요소들의 집합
    - 필드 : 속성, 컬럼
    - 레코드 : 튜플, 행(row)



### Model

- 장고는 모델을 통해 데이터에 접근하고 조작함.
- 사용할 데이터들의 필수적 필드와 동작을 포함
- 저장된 데이터의 구조(레이아웃)
- 데이터베이스와 파이썬 사이를 연결시켜주는 ORM
  - mapping: 하나의 값을 다른 값으로 대응시키는 것



- models.py의 class == 테이블의 스키마

- 각 모델은 django.models.Model 클래스의 서브 클래스

  - 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨

  ```django
  class Article(models.Model):
  	title = TextField() ...
  
  TextField보단 CharField가 용량 측면에서 좋다?(경량화)
  ```



## redirect

render 대신 쓰는거임

import render, redirect 해주고 쓰면됨

return redirect('url') 을 해주면 그냥 url페이지로 바로돌아감