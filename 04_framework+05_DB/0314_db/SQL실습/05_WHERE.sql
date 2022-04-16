-- 테이블(스키마)생성하기 -> import를 하면 csv 파일이 들어온다.
CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL);

-- 조회할 때 특정 조건으로 조회를 한다
-- users 테이블에서 age가 30 이상인 유저의 모든 칼럼을 조회한다면?
SELECT * FROM users WHERE age >= 30;
-- 동일 조건에서 이름만 조회한다면?
SELECT first_name FROM users WHERE age >= 30;

-- age가 30 이상이고 성이 '김'인 사람의 나이와 성만 조회하려면?
SELECT age, last_name, first_name FROM users WHERE age >= 30 AND last_name='김';