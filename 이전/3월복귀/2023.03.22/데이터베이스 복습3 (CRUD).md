# 데이터베이스 복습3 (CRUD)

create read update delete

레코드를 생성, 불러오기, 수정, 삭제



### INSERT

- INSERT INTO 테이블이름 (칼럼1, 칼럼2) VALUES (값1, 값2); 이런식으로 사용.
- 칼럼이 n개 있을때, 모든 칼럼에 맞춰 순서대로 입력하면 칼럼명은 안적어도 순서대로 가능.
  - INSERT INTO 테이블이름 VALUES (값1, 값2, .. , 값n);

- classmates 테이블에 이름이 홍길동이고 나이가 23인 데이터를 넣어보자. SELECT로 확인하기도.(1)
  - 당연히 텍스트는 '홍길동' 해줘야한다!

- **rowid**라고 id를 지정하지않아도 알아서 순차적으로 id를 넣어주는게 있다. (SQLite에서만)
  - SELECT rowid, * FROM ~~ 이런식으로 조회해보자.

- 여러명 넣으려면 ('기명', 25, '대구'), ('예원', 23, '대구') 이런식으로 콤마를 쓰자



### SELECT

- 조회를 하는데 다양한 절과함꼐 사용
  - ORDER BY, DISTINCT, LIMIT, WHERE...
- classmates 테이블에서 id, name 칼럼값만 조회하기.

- LIMIT : 특정칼럼 n개만 조회하고싶을떄.
- OFFSET : 특정칼럼의 N번째에 있는거 조회.
  - SELECT name FROM classmates LIMIT 1 OFFSET 3; : 위에서 3개 떨어진곳에 있는 하나의 레코드 조회
    - 즉 4번째 레코드가 나온다.
- WHERE : 특정칼럼의 특정 조건을 만족하는걸 조회
  - SELECT * FROM classmates WHERE address='서울'; 
  - SELECT name FROM classmates WHERE age >= 30;
  - 이런식으로 사용한다.

- DISTINCT : 중복을 없애서 조회하기.
  - **SELECT 다음에 DISTINCT를 적는다**
  - SELECT DISTINCT age FROM classmates;
    - 이러면 30살이 여러명이라도 하나만 뽑힌다.





### DELETE

- DELETE FROM classmates WHERE name='기명'; 
  - 이런식으로 사용한다.
  - 하나의 레코드를 지우는용으로 쓰인다. DROP은 테이블자체를 지우는것



### UPDATE (수정)

- UPDATE classmates SET address='서울' WHERE rowid=1;
  - rowid가 1인 사람의 주소를 서울로 바꾼다.
  - 이름이나 나이같은걸로 안하고 id로 하는이유는, 중복되는 이름이나 나이인 사람인경우도 있으므로.