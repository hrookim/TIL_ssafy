-- 조건에 따른 쿼리문
-- 1. 전체 인원 수
SELECT COUNT(*) FROM users_user;

-- 2. 나이가 30인 사람의 이름
SELECT first_name FROM users_user WHERE age=30;

-- 3. 나이가 30살 이상인 사람의 인원수
SELECT first_name FROM users_user WHERE age>=30;
SELECT COUNT(*) FROM users_user WHERE age>=30;

-- 4. 나이가 20살 이하인 사람의 인원수
SELECT COUNT(*) FROM users_user WHERE age<=20;

-- 5. 나이가 30이면서 성이 김씨인 사람의 인원수
SELECT COUNT(*) FROM users_user WHERE age=30 AND last_name='김';

-- 6. 나이가 30이거나 성이 김씨인 사람 / 인원수
SELECT first_name, last_name, age FROM users_user WHERE age=30 or last_name='김';

-- 7. 지역번호가 02인 사람의 인원수
SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';

-- 8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름 / 폰 번호
SELECT first_name FROM users_user WHERE country='강원도' AND last_name='황';
SELECT phone FROM users_user WHERE country='강원도' AND last_name='황';
