-- ALTER TABLE
-- 새 테이블 만들어서 값 추가하기
CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL);

INSERT INTO articles 
VALUES ('1번제목', '1번내용');

-- 테이블 이름 변경
ALTER TABLE articles RENAME TO news;

-- 테이블에 열 추가
ALTER TABLE news ADD COLUMN create_at TEXT NOT NULL;

-- 1. NOT NULL 없이 추가
ALTER TABLE news ADD COLUMN create_at TEXT ;
INSERT INTO news VALUES ('2번제목', '2번내용', datetime('now'));

-- 2. DEFAULT를 준다
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';

-- column 이름 수정
ALTER TABLE news RENAME COLUMN title TO name;

-- column 삭제
ALTER TABLE news DROP COLUMN subtitle;