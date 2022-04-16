-- 테이블 지우고 생성하기
DROP TABLE classmates;
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
    );


-- 레코드 넣기
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);

-- 모든 열에 값을 넣는 경우 특별히 컬럼을 지정하지 않아도 된다.
INSERT INTO classmates VALUES ('김혜림', 27, '서울시 양천구');

-- 원래대로라면, 전체 조회를 위해서는 아래 코드를 실행해야 한다.
SELECT rowid, * FROM classmates;


-- NOT NULL 설정 후 넣어보기
INSERT INTO classmates (name, age, address) VALUES ('공조한', 26, '인천시 부평구');


-- 테이블 지우고 생성하기, 우리는 이번 실습에서 rowid를 쓸거다 호홓
DROP TABLE classmates;
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
    );

-- INSERT 5명 넣어보기 
INSERT INTO classmates
VALUES
('김씨', 20, '서울'),
('우씨', 20, '서울'),
('곡씨', 20, '서울'),
('박씨', 20, '서울'),
('공씨', 20, '서울');