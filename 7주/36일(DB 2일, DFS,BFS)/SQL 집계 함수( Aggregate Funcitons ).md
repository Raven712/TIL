# SQL 집계 함수( Aggregate Funcitons )



- COUNT
  - 그룹의 항목 수 가져오기
- AVG
  - 모든 값 평균 계산
- MAX
- MIN
- SUM 



***

30세 이상인 사람의 수

- SELECT COUNT(*) FROM users WHERE age >= 30;



전체중에 가장 작은 나이

- SELECT MIN(age) FROM users; 



이씨중에 나이가 제일 작은것

- SELECT MIN(age) FROM users WHERE last_name = '이';
  - 이 사람의 이름까지 보고싶으면, MIN 뒤에 first_name 넣으면 됨
    - SELECT MIN(age), first_name FROM users WHERE last_name = '이';

30살 이상 사람들의 평균나이는?

- SELECT AVG(age) FROM users WHERE age >= 30;



계좌 잔액이 높은사람과 그 액수를 조회하기

- SELECT MAX(balance), last_name, first_name FROM users;





### LIKE

- 패턴 일치를 기반으로 데이터 조회하기.
- SQLITE는 2개의 와일드카드 제공
  - % : 0개 이상의 문자
  - _ : 임의의 단일 문자



- 예시
  - SELECT * FROM 테이블 WHERE 칼럼 LIKE '패턴';
    - 2% : 2로 시작하는 값
    - %2 : 2로 끝나는 값
    - %2% : 2가 들어가는 값
    - _2% : 아무값이 한개 있고 두번째가 2로 시작하는 값
    - 1___ : 1로 시작하고 총 4자리인 값
    - 2_% _% / 2__%  : 2로 시작하고 적어도 3자리인 값

지역번호가 02인 사람을 조회한다면?

- SELECT * FROM users WHERE phone LIKE '02-%';



users 테이블에서 이름이 '준' 으로 끝나는사람을 조회한다면?

- SELECT * FROM users WHERE first_name LIKE '%준';



users 테이블에서 중간번호가 5114인 사람을 조회하려면?

- SELECT * FROM users WHERE phone LIKE '%-5114-%';





### ORDER BY

- 조회 결과 집합을 정렬
- SELECT 문에 추가해서 사용
- 정렬 순서를 위한 키워드 2개 제공
  - ASC - 오름차순(기본)
  - DESC - 내림차순



users에서 나이순으로 오름차순 정렬해서 10개만 조회하면?

- SELECT * FROM users ORDER BY age ASC LIMIT 10;



잔액은 내림차순인데 성은 오름차순인 방법

- SELECT last_name, lastSEL_name, balnce FROM users ORDER BY balance DESC, last_name ASC 