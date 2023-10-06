# DB 1일_3(CRUD)

### CREATE

- INSERT

  - 테이블에 단일 행 삽입

    - INSERT INTO 테이블명 (컬럼1, 컬럼2) VALUES (값1, 값2);

  - 테이블에 정의 된 모든 컬럼에 맞춰 순서대로 입력

    - INSERT INTO 테이블명 VALUES (값1, 2, 3);

  - classmates 테이블에 이름이 길동이고 나이가 23인 데이터 넣기

    - INSERT INTO classmates (name, ages) VALUES ('길동', 23);

      

### READ

- SELECT

  - 테이블에서 데이터 조회

  - 다양한 조건을 붙이기 가능

    - LIMIT, WHERE(조건), SELECT DISTINCT(중복제거), OFFSET ..

    - classmates 테이블에서 id, name 컬럼 값만 조회하기

      - SELECT id, name FROM classmates;

    - 컬럼 값 하나만 조회하려면 ? 

      - SELECT id, name FROM classmates LIMIT 1;

    - 세번 째에 있는 하나만 조회 하기

      - SELECT id, name FROM classmates LIMIT 1 OFFSET 2;
        - OFFSET은 N칸을 띄우고, 그 다음을 출력하는거라서 2 해야함

    - 주소가 서울인 사람만 조회

      - SELECT id, name FROM classmates WHERE address='서울';

    - age값 전체를 중복없이 조회하기

      - SELECT DISTINCT age FROM classmates;

        - DISTINCT 는 SELECT 바로 뒤에 써야함

          

- DELETE

  - DELETE FROM classmates WHERE rowid=5;
    - rowid가 5인 레코드를 지움.

  

  

  

  

  

​	