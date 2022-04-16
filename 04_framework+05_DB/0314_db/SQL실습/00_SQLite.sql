-- SQLite 조작 연습을 시작하지.
SELECT * FROM examples;

-- 테이블 생성 (소문자로도 동작은 하지만 대문자로 사용하자)
-- 이것은 스키마를 작성하는 코드
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT 
    );

DROP TABLE classmates;

CREATE TABLE classmates (
  name TEXT,
  age INT,
  address TEXT
  );