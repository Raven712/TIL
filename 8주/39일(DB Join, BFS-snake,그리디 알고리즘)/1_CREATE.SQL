CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT,
    role_id INT     -- 테이블 생성 (CRUD의  C)
);


INSERT INTO users VALUES        -- 테이블에 값넣기 (CRUD -> U)
    (1, '관리자', 1),
    (2, '김철수', 2),
    (3, '이영희', 2);


CREATE TABLE articles (
    id INT PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INT
);

INSERT INTO articles VALUES        -- 테이블에 값넣기 (CRUD -> U)
    (1, '어드민', '111', 1),
    (2, '스태프', '111', 2),
    (3, '학생', '333', 1);