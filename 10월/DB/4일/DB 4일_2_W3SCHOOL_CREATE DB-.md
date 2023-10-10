# DB 4일_2 _ W3SCHOOL _ CREATE DB-

### CREATE

- CREATE DATABASE 데이터베이스
- CREATE TABLE 테이블명 (칼럼1 데이터타입, 칼럼2 ...);

### DROP

- DROP DATABASE 데이터베이스
- TRUNCATE << 테이블을 완전히 비우는거지만 삭제는 X.


### BACKUP

- BACKUP DATABASE 데이터베이스 TO DISK = '경로';



### ALTER TABLE

- 존재하는 테이블의 칼럼을 수정-추가-삭제 하려고 쓰는것
- ALTER TABLE 테이블명 ADD 칼럼명 데이터타입;
  - ALTER TABLE Customers ADD Email varchar(30);
  - RENAME으로 이름바꾸기도 됨

- DROP COLUMN으로 삭제 (ADD 자리에)

### CONSTRAINTS

- 테이블 데이터에 특정 룰을 만들려고 사용
- NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT 등



### DATE

- DATE : YYYY-MM-DD
- DATETIME : YYYY-MM-DD HH:MI:SS
  - TIMESTAMP도 같다
- YEAR : YYYY 