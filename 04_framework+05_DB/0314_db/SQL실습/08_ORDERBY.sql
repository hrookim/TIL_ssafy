-- ORDER BY

-- 나이 순으로 오름차순 정렬하여 상위 10개만 조회한다면?
SELECT * FROM users ORDER BY age LIMIT 10;

-- 나이 순, 성 순으로 오름차순 정렬하여 상위 10개 조회
SELECT * FROM users ORDER BY age, last_name LIMIT 10;

-- 계좌 잔액 순으로 내림차순 정렬, 성과 이름을 10개만 조회
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;