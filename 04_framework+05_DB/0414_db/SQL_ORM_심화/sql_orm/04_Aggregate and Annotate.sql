-- Aggregate and Annotate
-- 1. 전체 평균 나이
SELECT AVG(age) AS age_average FROM users_user;

-- 2. 김씨 사람들의 평균 나이 + 최대, 최소 나이
SELECT AVG(age) AS age_average FROM users_user WHERE last_name='김';
SELECT AVG(age), MAX(age), MIN(age), SUM(balance) FROM users_user WHERE last_name='김';

-- 3. 강원도에 사는 사람의 평균 계좌 잔고
SELECT AVG(balance) FROM users_user WHERE country='강원도';

-- 4. 계좌 잔액 중 가장 높은 값
SELECT MAX(balance) FROM users_user;

-- 5. 계좌 잔액 총액
SELECT SUM(balance) FROM users_user;


-- 1. 지역별 인원수
SELECT country, COUNT(*) AS country_count FROM users_user GROUP BY country;
