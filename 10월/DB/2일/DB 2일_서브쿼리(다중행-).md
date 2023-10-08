# DB 2일_서브쿼리(다중행-)

- 다중행 서브쿼리

- 서브쿼리 결과가 2개 이상인 경우

  - 이은정씨와 같은 지역에 사는 사람의 수는?

    - 이은정이 경상도에도 있고 전라도에도 있을수 있다

    - 이떄 IN, EXISTS 등의 연산자를 통해 해결

  - ```sql
    SELECT COUNT(*)
    FROM users
    WHERE country IN (
    	SELECT country
    	FROM users
    	WHERE first_name ='은정' AND last_name = '이'
    );
    # IN을 사용해서 모든 이은정이 사는 지역의 사람수를 측정가능케 함
    # IN 안쓰면 한 지역 합만 나옴
    ```



- 다중칼럼 서브쿼리

  - 특정 성씨에서 가장 어린 사람들의 이름, 나이는?

  - ```sql
    SELECT MIN(age), last_name, first_name 
    FROM users
    ```

    