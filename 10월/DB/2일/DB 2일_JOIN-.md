# DB 2일_JOIN-

- 여러개의 테이블을 결합해서 볼떄 필요한 것
- "관계형" 데이터베이스의 핵심 기능
- 보통 DB의 테이블은 하나의 테이블에 많은 데이터를 저장하지 않음.
  - 그걸 JOIN으로 활용
- 일반적으로 레코드는 PK, FK 값의 관계에 의해 결합함.



- INNER JOIN

  - 두 테이블에 모두 일치하는 행만 반환

  - ```SQL
    SELECT *
    FROM 테이블1 [INNER] JOIN 테이블2 # INNER 생략해도됨
    	ON 테이블1.칼럼 = 테이블2.칼럼;
    ```

  - 

- OUTER JOIN

  - 동일한 값이 없는 행도 반환

  - 기준 테이블 따라 LEFT, RIGHT, FULL을 지정

  - ```sql
    SELECT *
    FROM 테이블 1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2
    	ON 테이블1.칼럼 = 테이블2.칼럼;
    ```

- CROSS JOIN

  - 모든 데이터의 조합

  - ```SQL
    SELECT *
    FROM 테이블1 CROSS JOIN 테이블2;
    # 잘 쓰이진 않을듯
    ```

  - 