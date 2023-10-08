# DB 2일_1(WHERE,LIKE,ORDER BY~)

- WHERE 절을 할떄 연산자 우선순위
  - WHERE height = 175 OR height = 180 AND weight = 80;
  - 과 WHERE (height = 175 OR height = 180) AND weight = 80;
  - 은 확연히 다르다.
- 1순위 (), 2순위 NOT, 3순위 비교연산자, 4순위 AND, 5순위 OR 이기 때문



## 집계 함수 (Aggregate function)

- COUNT
- AVG
- MAX
- MIN
- SUM

ex) 계좌 잔액이 가장 많은 사람을 조회하려면?

- SELECT MAX(balance), first_name FROM users;
  - WHERE balance=MAX(balance) 이런건 하면 안된다 !



### LIKE

- % 는 0개이상의 문자를 포함한 것 (1개 아니다)
- _ 는 언더바 갯수만큼의 문자를 포함한 것.
- SELECT COUNT(*) FROM users WHERE last_name LIKE '김%';
  - 김~인 사람의 숫자를 추출
  - 문자열이라고 쌍따옴표를 쓰면 안된다.



### ORDER BY

- 말 그대로 정렬
- SELECT * FROM users ORDER BY ages LIMIT 10;
  - 나이 순 오름차순 정렬 10명 추출
  - 내림차순은 DESC