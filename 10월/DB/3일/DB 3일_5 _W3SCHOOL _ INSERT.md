# DB 3일_5 _W3SCHOOL _ INSERT~

### NULL

테이블의 필드가 선택적이면 아무것도 안넣고 레코드를 추가,업데이트 할수있음

- 그때 그 필드는 NULL이 됨



### UPDATE

- WHERE 생략하면 안되니 꼭 참고
- UPDATE 테이블 SET 칼럼 = 밸류, 칼럼2 = 밸류2 ..
  - WHERE 조건;

### DELETE

- 얘도 WHERE 생략 ㄴㄴ
- DELETE FROM 테이블 WHERE 조건



### 집계함수들

- COUNT 쓸때 DISTINCT 할거면 COUNT(DISTINCT ~) 해줘야함
- SUM() 할때 괄호안에 연산자를 넣을수도 있음
  - SELECT SUM(Quantity * 10) FROM OrderDetails;



### LIKE의 와일드카드

- []
  - [] 안에 있는것중 뭐라도 있으면 가져옴
    - WHERE CustomerName LIKE '[bsp]%';
    - b%든 s%든 p%든 다 가져온다는말

- -
  - range의 의미
    - WHERE CustomerName LIKE '[a-f]%';
    - a% b% c%... f% 다 가져온다는말

- !
  - NOT의 의미
    - WHERE CustomerName LIKE '[!a-f]%';
    - a...f 로 시작하는게 아닌걸 가져온다



### IN

- OR이랑 같음 WHERE절에 쓰는거
  - SELECT 칼럼 FROM 테이블 WHERE 칼럼 IN (밸류, 밸류2..);
- 반대는 NOT IN (하나라도 있으면 안된다)

- **서브쿼리**를 활용할수있다
  - SELECT * FROM Customers WHERE CustomerID 
    - IN (SELECT Customerid FROM Orders);



### BETWEEN

- WHERE절에 쓰는거, 반대는 NOT BETWEEN
- 꼭 숫자에만 쓰는게 아니고, TEXT에도 사용가능 (WHERE Name BETWEEN '머시기' AND '저시기';)
- 날짜에도 가능
  - SELECT * FROM Orders WHERE OrderDate BETWEEN '2020-02-02' AND '2021-02-02';



### AS

- 옵셔널한 친구임

- **,를 통해 칼럼들을 이어서 설정할수가 있음**

  - SELECT CustomerName, Address + ',' + PostalCode + '' + City + ',' + Country AS Address....

    