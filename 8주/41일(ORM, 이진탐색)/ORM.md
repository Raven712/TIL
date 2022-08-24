# ORM

- 파이썬으로 DB를 조작하는것.
- Object Relational Mapping 
- 파이썬에 내장 라이브러리 (SQLAlchemy, peewee등) 있고, 장고에선 내장 장고 orm 활용함



## 참고

```
python manage.py shell_plus # 셸 진입
***

python manage.py makemigrations

python manage.py migrate # 마이그레이션


***
python manage.py --version 버전확인(장고)

pip install -r requirements.txt  # 패키지설치


. venv/Scripts/activate # 가상환경 실행

```



객체로 DB 조작하기

- Genre.objects.all()  == Select * from Genre; 와 같음
  - 객체 리스트를 만들어서 반환해줌



### 모델 설계

- SQL의 Create Table genres( id primary key, name .....)

- (1) 클래스 생성해서 원하는 DB구조 만들기

```python
from django.db import models

class Genre(models.Model): # 장르 클래스 만드는데, models.Model 내부클래스를 상속받는것
    	#왜? -> 미리 만들어진 기능들을 활용하고 싶어서.
    name = models.CharField(max_length = 30)  # sql의 varchar (30) 
    
```



#### 마이그레이션

- model에 생긴 변화를 db에 반영하기 위한 방법
- 마이그레이션 파일을 만들어 db 스키마를 반영함.
  - makemigrations : 마이그레이션 파일 생성
  - migrate : 마이그레이션을 db에 반영

- ex) 클래스 생성- 테이블 생성 - 필드 변경 (crud) - 클래스 수정. 여기서 클래스 수정이 makemigrations -> migrate



- migrate 살펴보기

  - ```python
    begin;
    CREATE TABLE "db_genre" (
    	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    	"name" varchar(30) NOT NULL
    );
    COMMIT; # 트랜잭션
    ```



## ORM 기본조작 (shell 에서 하는것.)

- create
  - genre.objects.create(name = '발라드') 같은식으로
  - 혹은 genre = Genre()
    - genre.name = '락'
    - genre.save()  이렇게도 할수있음
- read
  - genre.objects.get(id = 1)
  - genre.objects.filter(id = 1) 차이가 뭘까 --> get은 단일객체(없거나 1개가아니면 오류)
    - ​	                                                              filter는 전체 쿼리셋(무조건 결과가 쿼리셋. 하나가 있어도 리스트 없으면 빈리스트)
    - 그럼 get은 언제쓰고 filter는 언제쓰나
      - get은 PK를 바탕으로 뭔가를 찾을때
      - filter는 나머지 모든상황

- update
  - genre = genre.objects.get(id = 1)
  - genre.name => '인디밴드' --> 이걸 '인디음악' 으로 바꾸고싶으면
    - genre.name = '인디음악'
    - genre.save()

- delete
  - genre = genre.objects.get(id = 1)
  - genre.name = '트로트'
  - genre.delete() < 이거하면바로끝남 (save 필요없음)



```python
from django.db import models

class Artist(models.Model):
    name = mdoels.CharField(max_length = 30)
    debut = models.DateField()
    
    --> python manage.py makemigrations
    python manage.py migrate
    
```

```python
# 아티스트 생성
artist = Artist()
artist.name = '아이브'

import datetime
artist.debut = datetime.date(2021, 12, 1)
artist.save()
```

