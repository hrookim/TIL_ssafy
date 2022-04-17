-- 기본 CRUD 로직
-- 1. 모든 user 레코드 조회
SELECT * FROM users_user;

-- 2. user 레코드 생성
INSERT INTO users_user 
VALUES
(101, '혜림', '김', 27, '서울', '010-1234-5678', 10000000);

-- user 레코드 삭제
DELETE FROM users_user WHERE id=101;

-- 3. user 레코드 조회
SELECT * FROM users_user WHERE id=101;

-- 4. 해당 레코드 수정
UPDATE users_user SET first_name='조한', last_name='공' WHERE id=101;

