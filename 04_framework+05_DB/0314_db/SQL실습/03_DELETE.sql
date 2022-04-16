-- SQLite
DELETE FROM classmates WHERE rowid=5;

-- DELETE 이후 id확인
INSERT INTO classmates VALUES ('한씨', 21, '전주');
SELECT rowid, * FROM classmates;