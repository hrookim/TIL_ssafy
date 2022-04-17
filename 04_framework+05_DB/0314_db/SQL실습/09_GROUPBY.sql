-- GROUP BY

-- users에서 각 성씨가 몇 명씩 있는지 조회한다면?
SELECT last_name, COUNT(*) FROM users GROUP BY last_name; 

-- users에서 각 성씨가 몇 명씩 있는지 조회한다면?
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name; 

-- 컬럼이 여러개 존재하는 경우
SELECT country, last_name, COUNT(*)  FROM users GROUP BY country, last_name;