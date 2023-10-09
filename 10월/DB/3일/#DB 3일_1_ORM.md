# DB 3일_ORM

- 객체
  - 속성, 메서드를 가지고 있음
  - 속성은 값
  - 메서드는 함수
- 클래스
  - 틀
  - 인스턴스는 그 안의 사례 같은거



## ORM

- 객체-관계-매핑

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간 데이터를 변환하는 프로그래밍 기술
- 파이썬에서는 SQLAlchemy, peewee등 라이브러리가 있고 장고 프레임워크에서는 내장 장고 ORM을 활용



- 객체로 DB를 조작한다
  - Genre.objects.all()
  - class Genre(models.Model):
    - name = models.CharField(max_length=30)
  - 위의 문장은 SQL의 CREATE TABLE genre 같은것



- Migration
  - Model에 생긴 변화를 DB에 반영하는 방법
  - 마이그레이션 파일을 만들어 DB 스키마에 반영
    - python manage.py makemigrations - 마이그레이션생서
    - python manage.py migrate - 마이그레이션 DB반영



- DB 조작
  - Genre.objects.all()
    - Genre = 클래스 이름
    - objects = 도구
    - all = 쿼리셋 API