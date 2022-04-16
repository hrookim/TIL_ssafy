-- LIKE
-- 20대인 사람만 조회
SELECT * FROM users WHERE age LIKE '2_' ;

-- 지역번호 02인 사람만 조회
SELECT first_name, phone FROM users WHERE phone LIKE '02-%'; 

-- 이름이 '준'으로 긑나는 사람만 조회한다면
SELECT * FROM users WHERE first_name LIKE '%준';

-- 중간 번호가 5114인 사람만 조회한다면
SELECT first_name, phone FROM users WHERE phone LIKE '%-5114-%';