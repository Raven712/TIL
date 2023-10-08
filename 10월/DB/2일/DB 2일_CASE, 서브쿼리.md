# DB 2일_CASE

- 특정 상황에서 데이터를 변환해서 활용 할 수 있음
- ELSE를 생략하는 경우 NULL 값 지정

```sql
CASE
	WHEN 조건식 THEN 식
	WHEN 조건식 THEN 식
	ELSE 식
END
# 파이썬의 if문과 유사하다
# 사용 예시
# gender = 1(남),2(여) 라고 되어있을때 1이면 남, 2면 여로 출력하고싶다. 
SELECT 
	id, 
	CASE
    	WHEN gender = 1 THEN '남자',
        WHEN gender = 2 THEN '여자'
    END AS 성별 # AS 성별을 넣지 않으면 id, CASE 로 출력됨. CASE를 성별로 명명해야 보기좋으니까..
FROM users
LIMIT 5;

# 비슷하게, WHEN 절에 등호가 아닌 구간을 지정할수도 있다. 흡연지수 0~20 비흡연 이런식..
```



## 서브쿼리

- 특정 값을 메인쿼리에 반환해 활용
- 실제 테이블에 없는 기준을 이용한 검색을 가능하게 함
- 소괄호로 감싸서 사용..



- 단일행 서브쿼리
  - 서브쿼리 결과가 0, 1개인 경우
  - 단일행 비교 연산자와 사용 (>=, >, = ...)

```sql
# 나이가 가장 적은 사람의 수를 뽑으려면?

SELECT MIN(age)
FROM users
# 얘가 테이블의 최소 나이

SELECT COUNT(*)
FROM users
WHERE age = (SELECT MIN(age) FROM users);

# 그걸 그대로 넣어줌

# Q1. users에서 평균 계좌 잔고보다 잔액이 많은 사람의 수는?

SELECT AVG(balance)
FROM users
# 평균

SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

# Q2. users에서 유은정과 같은 지역에 사는 사람의 수는?

# 유은정의 지역?
SELECT country
FROM users
WHERE first_name = '은정' AND last_name = '유'

SELECT COUNT(*)
FROM users
WHERE country = (SELECT country FROM users WHERE first_name = '은정' AND last_name = '유');

```

