[TOC]

# SQL with django ORM

## 기본 준비 사항

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
    $ python manage.py migrate
    ```
  
* 제공 받은 `users.csv` 파일은 db.sqlite3와 같은 곳에 위치하도록 이동

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ sqlite3 db.sqlite3
    ```

  * 테이블 확인

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    ```
    
  * csv 파일 data 로드 및 확인

    ```sqlite
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```



---



## 문제

> ORM은 django extensions의 shell_plus에서,
>
> SQL은 수업에서 진행한 [SQLite 확장프로그램](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) 사용 방식으로 진행

### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   from users.models import User
   
   User.objects.all()
   ```

      ```sql
   -- sql
   
   SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   # 1.
   User.objects.create(first_name='혜림', last_name='김', age=27, country='서울', phone='010-1234-5678', balance=10000000)
   
   # 2.
   user=User(first_name='혜림', last_name='김', age=27, country='서울', phone='010-1234-5678', balance=10000000)
   user.save()
   
   # 3.
   user = User()
   user.first_name = '혜림'
   ...
   user.save()
   ```

   ```sql
   -- sql
   INSERT INTO users_user 
   VALUES
   (101, '혜림', '김', 27, '서울', '010-1234-5678', 10000000);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   # orm
   user = User.objects.get(id=102)
   ```

   ```sql
   -- sql
   SELECT * FROM users_user WHERE id=102;
   ```

4. 해당 user 레코드 수정

   - ORM: `102` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `102` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   user = User.objects.get(id=102)
   user.last_name = '김'
   user.save()
   ```

      ```sql
   -- sql
   UPDATE users_user SET first_name='철수', last_name='김' WHERE id=102;
      ```

5. 해당 user 레코드 삭제

   - ORM: `102` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 

   ```python
   # orm
   user = User.objects.get(id=102)
   user.delete()
   ```
   
   ```sql
   -- sql
   DELETE FROM users_user WHERE id=102;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   User.objects.all().count()  # DB가 100을 응답
   
   len(User.objects.all())		# DB가 전체 객체를 응답, 이후에 count
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user;
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values('컬럼이름')`

   ```python
   # orm
   User.objects.filter(age=30)		# 객체들이 나옴
   User.objects.filter(age=30).values('first_name')	# 해당 열만 나옴
   ```

   > 최적화를 할 때, 사용될 수 있다. 전체 객체들을 다 뽑는 것이 아니라 필요한 열만 가지고 올 수 있는 것이다.

   <img src="SQL_ORM.assets/image-20220414153242638.png" alt="image-20220414153242638" style="zoom:67%;" />

   <img src="SQL_ORM.assets/image-20220414153408952.png" alt="image-20220414153408952" style="zoom:67%;" />

      ```sql
   -- sql
   SELECT first_name FROM users_user WHERE age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   User.objects.filter(age__gte=30).count()
   ```

   <img src="SQL_ORM.assets/image-20220414154202453.png" alt="image-20220414154202453"  />

   > `age >= 30`가 사용 불가인 이유!?
   >
   > 저 위치는 메소드에 인자를 넣는 곳이기 때문에, 저런 표현식을 넘겨서는 안된다!!

      ```sql
   -- sql
   -- 이름 출력
   SELECT first_name FROM users_user WHERE age>=30;
   -- 인원수 출력
   SELECT COUNT(*) FROM users_user WHERE age>=30;
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   User.objects.filter(age__lte=20).count()
   ```

   ![image-20220414154240754](SQL_ORM.assets/image-20220414154240754.png)

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age<=20;
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   User.objects.filter(age=30, last_name='김')
   User.objects.filter(age=30, last_name='김').count()
   ```

   ![image-20220414154447105](SQL_ORM.assets/image-20220414154447105.png)

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age=30 AND last_name='김';
      ```

6. ***나이가 30이거나 성이 김씨인 사람?**

   ```python
   # orm
   from django.db.models import Q
   User.objects.filter(Q(age=30) | Q(last_name='김'))
   ```

   ![image-20220414155057878](SQL_ORM.assets/image-20220414155057878.png)

   ![image-20220414154952280](SQL_ORM.assets/image-20220414154952280.png)

   > 이것도 가능하긴 한데, 조건이 많아질수록 코드가 너무 길어진다. 그래서 Q를 사용한다.

   ```sql
   -- sql
   SELECT first_name, last_name, age FROM users_user WHERE age=30 or last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   User.objects.filter(phone__startswith='02')
   User.objects.filter(phone__startswith='02').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user 
   WHERE phone LIKE '02-%'
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   User.objects.filter(last_name__startswith='황', country='강원도').values('first_name')
   ```
   
      ```sql
   -- sql
   SELECT first_name FROM users_user WHERE country='강원도' AND last_name='황';
      ```



9. 거주 지역이 강원도이면서 성이 황씨인 사람의 핸드폰 번호

   ```python
   # orm
   User.objects.filter(last_name__startswith='황', country='강원도').values('phone')
   
   # 이거는 안된다! 왜냐면 쿼리셋이기 때문에 객체로 생각해서 phone으로 접근할 수가 없다
   # filter의 결과는 쿼리셋이어서 안된다!!!! -> 리스트 형태로 옴
   User.objects.filter(last_name__startswith='황', country='강원도').phone
   ```

   

---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   Users.objects.order_by('age')  # 오름차순
   Users.objects.order_by('-age') # 내침차순
   ```

   ![image-20220414160425317](SQL_ORM.assets/image-20220414160425317.png)

   ![image-20220414160521016](SQL_ORM.assets/image-20220414160521016.png)

   > 전체를 다 가져와서 10개만 보여주는 것이 아닌, 실제로 쿼리가 10개 리밋을 정해서 들어갔다

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY balance LIMIT 10;
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   
   User.objects.order_by('balance', '-age')[:10]
   ```
   
   ```sql
   -- sql
   SELECT * FROM users_user ORDER BY balance, age DESC LIMIT 10;
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   User.objects.order_by('-last_name', '-first_name')[4]  # 단일 객체 된다
   ```
   
   > 그래서 개체의 속성에 접근하는 것도 가능하다.
   >
   > <img src="SQL_ORM.assets/image-20220418012608381.png" alt="image-20220418012608381" style="zoom:70%;" />
   
   > 길이가 1로 지정되면 단일 객체가 되기 때문에, query를 인쇄해서 볼 수 없다 (신기방기)
   >
   > 인덱스로 해서 길이가 2 이상이 되면 쿼리셋으로 반환이 되어서 쿼리를 인쇄해서 볼 수 있다
   >
   > ![image-20220418012909703](SQL_ORM.assets/image-20220418012909703.png)
   
      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
      ```



---



### 4. 표현식

#### 4.1* Aggregate

> - https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
>- '종합', '집합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용
>- `Django_aggregation.md` 문서 참고

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   
   User.objects.aggregate(Avg('age'))
   # {'age__avg': 28.23} => default가 col + __avg
   
   User.objects.aggregate(age_average = Avg('age'))
   # {'age_average': 28.23}
   ```

      ```sql
   -- sql
   SELECT AVG(age) AS age_average FROM users_user;
      ```

2. 김씨의 평균 나이 (+ 최대, 최소 나이)

   ```python
   # orm
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   
   from django.db.models import Avg, Max, Min  # 사실 이미 되어 있음
   User.objects.filter(last_name='김').aggregate(Avg('age'), Max('age'), Min('age'), Sum('balance'))
   ```

   ![image-20220414165217691](SQL_ORM.assets/image-20220414165217691.png)

   > ![image-20220418010737094](SQL_ORM.assets/image-20220418010737094.png)
   >
   > 그래서 이렇게 get 메소드나 key로 접근이 가능하다!

      ```sql
   -- sql
   SELECT AVG(age) AS age_average FROM users_user WHERE last_name='김';
   SELECT AVG(age), MAX(age), MIN(age), SUM(balance) FROM users_user WHERE last_name='김';
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   User.objects.filter(country='강원도').aggregate(Avg('balance'))
   # {'balance__avg': 157895.0}
   ```

   ```sql
   -- sql
   SELECT AVG(balance) FROM users_user WHERE country='강원도';
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   User.objects.aggregate(Max('balance'))
   ```

      ```sql
   -- sql
   SELECT MAX(balance) FROM users_user;
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   User.objects.aggregate(Sum('balance'))
   ```
   
      ```sql
   -- sql
   SELECT SUM(balance) FROM users_user;
      ```



#### 4.2 Annotate

1. 지역별 인원 수

   ```PYTHON
   # orm
   User.objects.values('country').annotate(Count('country'))
   ```
   
   ![image-20220414170419564](SQL_ORM.assets/image-20220414170419564.png)
   
   ```SQL
   -- sql
   SELECT country, COUNT(*) AS country_count FROM users_user GROUP BY country;
   ```
   
   | country  | country__count |
   | -------- | -------------- |
   | 강원도   | 14             |
   | 경기도   | 9              |
   | 경상남도 | 9              |
   
   