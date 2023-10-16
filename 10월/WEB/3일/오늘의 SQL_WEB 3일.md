# 오늘의 SQL_WEB 3일



**DATE_FORMAT(A.COLUMN, '%Y-%M-%D') AS ALIAS 절은 자주 사용하니 꼭 기억하자**

!!!!!!!!!!!!!!!!!!!!







LIKE로 조건 여러개를 걸고싶을때, OR를 쓰는건 맞지만 그때 칼럼을 다 따로 써줘야 한다

```SQL
WHERE MCDP_CD LIKE 'CS' OR MCDP_CD LIKE 'GS'

그냥 WHERE MCDP_CD LIKE 'CS' OR 'GS' 이렇게하면 안됨!!!
```

