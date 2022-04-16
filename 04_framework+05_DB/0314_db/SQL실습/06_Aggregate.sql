-- COUNT
-- users 테이블의 레코드 총 개수를 조회
SELECT COUNT(*) FROM users;

-- 30살 이상인 사람들의 평균 나이는?
SELECT AVG(age) FROM users WHERE age >= 30;

-- 계좌 잔액이 가장 높은 사람과 그 액수는?
SELECT first_name, MAX(balance) FROM users;

-- 30살 이상인 사람들의 평균 잔액은?
  SELECT AVG(balance) FROM users WHERE age >= 30;

