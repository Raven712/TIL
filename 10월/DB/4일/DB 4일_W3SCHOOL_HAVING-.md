# DB 4일_ W3SCHOOL _ HAVING-

### HAVING

- HAVING은 WHERE절에서 집계함수를 쓸수없어서 쓰는 절이다
- SELECT 칼럼 FROM 테이블 WHERE 조건 GROUP BY 칼럼 HAVING 조건 ORDER BY 칼럼
  - 이게 최종본임



### EXISTS

- 서브쿼리에 어떤 레코드라도 있는지 확인해보려고 사용된다 (한개이상이면 TRUE판정)
  - SELECT 칼럼 FROM 테이블 WHERE EXISTS (SELECT 칼럼 FROM 테이블 WHERE 조건);



### CASE

- IF 문 같은것

  ```sql
  CASE
  	WHEN 조건 THEN 결과1
  	WHEN 조건2 THEN 결과2
  	ELSE 결과
  END;
  # 예를 들어보자
  SELECT OrderID, Quantity,
  CASE
      WHEN Quantity > 30 THEN 'The quantity is greater than 30'
      WHEN Quantity = 30 THEN 'The quantity is 30'
      ELSE 'The quantity is under 30'
  END AS QuantityText
  FROM OrderDetails;
  
  그 외에 ORDER BY 다음에 조건문을 넣는식으로 사용도 가능하다
  ```

  

### ISNULL, IFNULL

- NULL값이 존재하는 필드와 그렇지않은 필드끼리 혼합계산을 할떄
  - NULL이 있으면 곱셈같은경우 NULL이 출력되는데, 그런경우 ISNULL, IFNULL을 통해 해결가능
  - SELECT ProductName, UnitPrice * (UnitInStock + ISNULL(UnitsOnOrder, 0))
  - 이런식으로