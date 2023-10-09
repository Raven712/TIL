# DB 3일_6 _ W3SCHOOL _JOIN-



## JOIN

- JOIN은 서로관계있는 둘이상의 테이블을 연결할때 씀

- 교집합을 연결할땐 INNER JOIN
  - 기타 LEFT, RIGHT, FULL

- 그리고 JOIN ~~ ON ~~ 의 양식을 지켜야함.
  - SELECT 칼럼 FROM 테이블1 (INNER...) JOIN 테이블2 ON 테이블1.칼럼 = 테이블2. 칼럼;

### INNER JOIN

- 교집합 추출
- INNER JOIN만큼은 INNER를 생략해도 된다

### FULL (OUTER) JOIN

- 합집합 추출
- OUTER 생략해도 됨



## GROUP BY

- GROUP BY는 집계함수와 자주 쓰임 (애초에 그러지않으면 의미가 별로없다)
- SELECT 칼럼 FROM 테이블 WHERE 조건 GROUP BY 칼럼 ORDER BY 칼럼;