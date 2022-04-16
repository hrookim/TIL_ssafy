-- GROUP BY

-- users에서 각 성씨가 몇 명씩 있는지 조회한다면?
SELECT last_name, COUNT(*) FROM users GROUP BY last_name; 

-- users에서 각 성씨가 몇 명씩 있는지 조회한다면?
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name; 