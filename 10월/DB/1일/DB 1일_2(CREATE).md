# DB 1일_2(CREATE~)

```sqlite
CREATE TABLE classmates (
	id INTEGER PRIMARY KEY,
	name TEXT
);
```

- .tables
  - 테이블 목록 조회
- .schema classmates
  - classmates 라는 스키마 조회
  - 위의 내용이 다 나옴
- INSERT INTO classmates VALUES (1, '복길');
  - 값 추가하기
  - id는 1, name은 복길인 값이 추가된것
- SELECT * FROM classmates;
  - classmates의 모든 값 조회

- DROP TABLE classmates;
  - classmates라는 테이블 삭제



## 테이블 생성, 삭제

- 필드(컬럼) 제약 조건

  - NOT NULL : NULL 입력금지
  - UNIQUE : 중복값 금지 (NULL은 중복가능)
  - PRIMARY KEY : NOT NULL + UNIQUE
  - FOREIGN KEY : 외래 키. 다른 테이블의 키
  - CHECK : 조건으로 설정된 값만 입력 허용
  - DEFAULT : 기본설정 값

- ```sqlite
  CREATE TABLE students(
  	id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      age INTEGER DEFAULT 1 CHECK (0 < age)
  );
  id는 숫자면서 PK (유일한값)
  이름은 글자면서 비어있는건 불가(없는거)
  나이는 숫자면서 기본값은 1이고 0보다 많은지 체크하라
  ```

  