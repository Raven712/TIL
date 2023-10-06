# CRUD

C : INSERT -- >INSERT INTO 테이블이름 ( 칼럼1,2...) VALUES (값1,2);

R : SELECT -- > SELECT * FROM 테이블이름 WHERE 조건;

U : UPDATE -- > UPDATE 테이블이름 SET 컬럼1 = 값 1, 컬럼2 = 값2, WHERE 조건;

D : DELETE -- >DELETE FROM 테이블이름 WHERE 조건;





## WHERE

users 테이블의 나이 30이상인 사람 출력하기

- SELECT * FROM users WHERE age >= 30; 
- 동일 조건에서, 이름만 뽑아내고싶다면?
  - SELECT first_name FROM users WHERE age >= 30;
  - 여기서, 또 3명만 뽑고싶다면?
    - SELECT first_name FROM users WHERE age >= 30 LIMIT 3;



users 테이블에서 age가 30이상이고 성이 '김' 인 사람의 나이와 성만 조회하기

- SELECT age, last_name FROM users WHERE age >= 30 and last_name = '김';



### WHERE 절의 연산자

- 비교 연산자
  - = 뺴고는 파이선과 같음.
- 논리 연산자
  - AND, OR, NOT
    - NOT : 뒤에 오는 조건의 결과를 반대로



### SQL 에서 사용할수 있는 연산자?

- BETWEEN A AND B
  - A, B사이를 비교
- IN (값1, 값2 ,..)
  - 목록중 값이 하나라도 일치하면 성공

- LIKE
  - 비교문자열과 형태 일치
  - 와일드카드 (% : 0개 이상 문자, _ : 1개 단일 문자)
- IS NULL /IS NOT NULL
  - NULL 여부 확인시 항상 = 대신 IS 사용



- 부정 연산자
  - !=, ^=, <> 모두 동일함
  - NOT 칼럼명 =  : ~와 같지않음



### 연산자 우선순위

1. 괄호
2. NOT
3. 비교연산자와 sql 연산자
4. AND
5. OR