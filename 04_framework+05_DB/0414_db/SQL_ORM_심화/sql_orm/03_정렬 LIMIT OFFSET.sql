-- 정렬 LIMIT OFFSET
-- 1. 나이가 많은 순으로 10명
SELECT * FROM users_user ORDER BY age DESC LIMIT 10;

-- 2. 잔액이 적은 순으로 10명
SELECT * FROM users_user ORDER BY balance LIMIT 10;

-- 3. 잔고는 오름차순, 나이는 내림차순으로 10명
SELECT * FROM users_user ORDER BY balance, age DESC LIMIT 10;

-- 4. 성, 이름 내림차순으로 5번째 있는 사람
SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
