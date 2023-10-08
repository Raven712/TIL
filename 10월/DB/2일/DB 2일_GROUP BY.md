# DB 2일_GROUP BY

- 행 집합에서 요약 행 집합을 만듦
- WHERE 절 뒤에 작성해야함 반드시
- 집계함수(COUNT, AVG, MAX, MIN, SUM)와 함께 이용할때 의미가 있음 !!!!
- SELECT AVG(ages) FROM users GROUP BY last_name;
  - 김,박,이... 등등의 성씨들마다의 평균나이가 추출됨



- 100번 이상 등장한 성을 출력하고싶을때, GROUP BY에 WHERE(조건) 을 넣고싶으면,

  HAVING을 써야한다. (순서의 문제 떄문..)

- SELECT last_name, COUNT(last_name) FROM users GROUP BY last_name HAVING COUNT(last_name) > 100;



**SELECT 문의 실행 순서**

- FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY



## ALTER TABLE

- 테이블 이름변경
  - ALTER TABLE users RENAME TO 새이름;
- 칼럼 추가
  - ALTER TABLE users ADD COLUMN 칼럼정의;
- 칼럼 이름수정
  - ALTER TABLE users RENAME COLUMN 지금이름 TO 새이름;
- 칼럼 삭제
  - ALTER TABLE users DROP COLUMN 지정칼럼;