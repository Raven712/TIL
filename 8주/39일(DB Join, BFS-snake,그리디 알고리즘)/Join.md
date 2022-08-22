# Join



- 관계형 db의 가장큰 장점이며 핵심적 기능
- db는 여러테이블로 나눠서 데이터를 저장하는데, 이걸 결합하는 기능임.
- 일반적으로 레코드는 기본키 PK나 외래키 FK 값의 관계에 의해 결합





- Inner join : 두 테이블에 모두 일치하는 행만 반환 ( 교집합 )
- outer join : 동일한 값이 없는 행도 반환
- cross join : 모든 데이터 조합



**여러개 JOIN 하려면 SELECT ~  FROM ~ JOIN ON ~ JOIN ON ~ 하면 됨**

- SELECT * FROM articles JOIN users ON articles.user_id = users.id JOIN role ON users.role_id = role.id; 



### Inner join

- SELECT * FROM 테이블1 [INNER] (생략) JOIN 테이블2 ON 테이블1.칼럼 = 테이블2.칼럼;

   - 예를들어, users테이블의 role_id칼럼 내용과 role 테이블의 id칼럼내용이 같은걸 원한다 ->

     - Select * FROM users JOIN role ON users.role_id = role.id;
        - Select * FROM users JOIN role ON users.role_id = role.id WHERE role.id = 2; --> 스태프(2) 만 출력.
        - Select * FROM users JOIN role ON users.role_id = role.id ORDER BY users.name DESC; (이름 내림차순 --> 그냥 name으로 order by 하는게 아니고, users.name 을 참고하는것!)

     

     

### OUTER JOIN

- LEFT ,RIGHT OUTER JOIN
- 예를들어 ID가 NULL일때, 그사람 정보에 대한 레코드가 전부 NULL이 되게하는것
  - SELECT * FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2 ON 테이블1.칼럼 = 테이블2.칼럼;
  - SELECT * FROM articles LEFT OUTER JOIN users ON articles.user_id = users.id;
  - NULL을 뺴고싶으면?
    - SELECT * FROM articles LEFT OUTER JOIN users ON articles.user_id = users.id WHERE articles.user_id IS NOT NULL;

- FULL OUTER JOIN은 합집합을 만들어냄



### CROSS JOIN

- SELECT * FROM 테이블1 CROSS  JOIN 테이블2; 

- 모든 가능한 경우의 수를 다 만들어냄