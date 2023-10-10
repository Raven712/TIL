# DB 4일_ 실습_ 프로그래머스

## SELECT

#### 인기있는 아이스크림

- ORDER BY를 여러번 할때는 , 로 구분을 지어줘야한다
  - ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;



### 조건에 부합하는 중고거래

- 두가지 테이블을 참조하고, 특정테이블의 내용을 따로따로 조회할때는
  - A.칼럼, B.칼럼 이런식으로 조회해야한다
    - SELECT A.REPLY, B.REPLY ,.... 

```sql
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_REPLY AS R
ON B.BOARD_ID = R.BOARD_ID
WHERE B.CREATED_DATE LIKE '2022-10%' AND R.CREATED_DATE LIKE '2022-10%'
ORDER BY R.CREATED_DATE ASC, B.TITLE ASC;
```

**DATE_FORMAT(A.COLUMN, '%Y-%M-%D') AS ALIAS 절은 자주 사용하니 꼭 기억하자**