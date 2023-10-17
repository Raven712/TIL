# 오늘의 SQL

집계함수와 HAVING절을 쓰는 양식을 까먹지 말자



## 가격이 제일 비싼 제품의 정보 출력하기

SELECT * FROM TABLE

까지는 맞는데

가격이 제일 비싼 제품을 어떻게 고르냐에 대해 생각을 했다

물론 ORDER BY PRICE DESC LIMIT 1; 이라는 꼼수도 있지만 집계함수를 사용해서 푸는게 맞다고 보았다



WHERE PRICE = MAX(PRICE) ?

이렇게 하면 오류가 난다.

HAVING을 쓴다? 집계함수를 쓰고 조건을 거니까 자꾸 HAVING에만 초점이 쏠렸는데 HAVING을 쓰는게 아니고 서브쿼리를 쓰는 문제였다



WHERE PRICE = (SELECT MAX(PRICE) FROM TABLE)



## 그 외 안것

1. 첫번쨰 SELECT문에 집계함수를 써도 인식이 된다..