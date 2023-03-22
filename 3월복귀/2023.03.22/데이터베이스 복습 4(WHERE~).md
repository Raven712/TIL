# 데이터베이스 복습 4(WHERE~)

- 복습
- C : INSERT
  - INSERT INTO 테이블이름 (칼럼..., 칼럼) VALUES (값1,2..);
- R : SELECT
  - SELECT * FROM 테이블이름 WHERE 조건;
- U: UPDATE
  - UPDATE 테이블이름 SET 칼럼1=값1, 칼럼2=값 WHERE 조건;
- D : DELETE
  - DELETE FROM 테이블이름 WHERE 조건;



## WHERE

- 비교 연산자 사용가능 (> = <..)
- 논리 연산자 사용가능
  - AND, OR, NOT(뒤에 오는 조건의 결과를 반대로)
  - SELECT * FROM classmates WHERE NOT ~



- BETWEEN A AND B 
  - BETWEEN 값1 < 비교값 < 값2 이런식
- IN (값1, 값, ...)
  - 목록중 값이 하나라도 일치하면 성공
- LIKE 
  - 비교 문자열과 형태 일치
  - 와일드카드 (% : 0개이상 문자, _ : 1개 단일문자)

- IS NULL / IS NOT NULL
  - **NULL 여부를 확인할떄는 =이 아니라 IS를 써야한다! **

- 부정 연산자
  - !=, ^=, <> 다 가능
  - NOT 칼럼명 = (~와 같지않다) 도 가능



- 연산자 우선순위
  - 1순위 괄호
  - 2순위 NOT
  - 3순위 비교 (BETWEEN..)
  - 4순위 AND
  - 5순위 OR