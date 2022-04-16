-- SELECT문 연습!!
SELECT rowid, name FROM classmates;

-- LIMIT 연습
SELECT * FROM classmates LIMIT 3;

-- LIMIT(개수) + OFFSET(몇번부터인지?)
SELECT rowid, name FROM classmates LIMIT 1  OFFSET 2 ;

-- WHERE
SELECT rowid, name FROM classmates WHERE address='서울';

--DISTINCT
SELECT DISTINCT age FROM classmates;