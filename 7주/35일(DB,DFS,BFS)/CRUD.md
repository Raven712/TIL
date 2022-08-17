#  CRUD

create read update delete.



### CREATE

- INSERT
  - 'insert a single row into a table'
  - 테이블에 단일 행 삽입
    - INSERT INTO 테이블이름 (컬럼1, 2) VALUES (값1, 2);

- classmates 테이블에 이름이 홍길동, 나이가 23인 데이터를 넣어보자. SELECT 문으로 확인하자.

``` sqlite
CREATE TABLE classmates (
	name TEXT,
    age INT,
	address TEXT
);

INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;
```

​	

### READ

- SELECT
  - 테이블에서 데이터 조회
  - SELECT 문은 sqlite에서 가장 기본이 되는문. 

- classmates 테이블에서, id name 컬럼값만 조회하기.
  - SELECT rowid, name FROM classmates;			rowid는 입력안해도 자동으로 등록됨



- classmates 테이블에서, id name 컬럼 값 하나만 조회하기.
  - SELECT rowid, name FROM classmates LIMIT 1;	<< 1은 rowid가 1인사람만 본다는것



- classmates 테이블에서, id, name 컬럼 값을 세번째에 있는 하나만 조회하기
  - SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;  << 
  - 두칸을 띄우고 보겠다. ( 1--> 2칸띄우기 =3)
  - 저기서 LIMIT의 숫자가 바뀌면, 3번쨰부터 LIMIT 뒤에 적힌 숫자만큼의 컬럼들을 보겠다는것 
    - LIMIT 3 OFFSET 2 << 이렇게하면, 3번쨰부터 3, 4, 5번 칼럼들을 보는것..



- classmates 테이블에서 id, name 컬럼 값중 주소가 서울인 경우의 데이터 조회하기
  - SELECT rowid, name FROM classmates WHERE address = '서울';

  - SELECT * FROM classmates WHERE address = '서울'; 도 됨. 

    

  

- **WHERE 뒤에 조건식들이 막 올수있는데, 파이썬처럼 AND, OR, NOT 다 됨.  연산자가 동일함! **





- - 별표는 "모든" 이라는 뜻임.  즉 모든 컬럼들을 다 SELECT (보겠다) 는것.



- classmates 테이블에서 age값 전체를 중복없이 조회하기.
  - SELECT DISTINCT age FROM classmates;



### DELETE

- DELETE FROM classmates WHERE rowid = 5; 이런거 가능 (하나의 레코드만 지우기.)



### UPDATE

- UPDATE classmates SET address='서울' WHERE rowid=5;
- SELECT rowid, * FROM classmates;