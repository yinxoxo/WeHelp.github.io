Assignment - Week 5
===
# Task 2

- Create a new database named website.
```sql=
CREATE DATABASE website;
```
- Create a new table named member, in the website database
```sql=
CREATE TABLE member(
         id BIGINT PRIMARY KEY AUTO_INCREMENT,
         name VARCHAR(255) NOT NULL,
         username VARCHAR(255) NOT NULL,
         password VARCHAR(255) NOT NULL,
         follower_count INT UNSIGNED NOT NULL DEFAULT 0,
         time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
     );
```
![圖片](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t2%E5%BB%BA%E7%AB%8B%E5%87%BA%E4%BE%86%E7%9A%84%E8%A1%A8%E6%A0%BC.png)
---
# Task 3

- INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
```sql=
INSERT INTO member(name, username,password)VALUES('test','test','test');
INSERT INTO member (name, username, password, follower_count ) VALUES
    -> ('mew1','usermew1','password1',67),
    -> ('mew2','usermew2','password2',100),
    -> ('mew3','usermew3','password3',88),
    -> ('mew4','usermew4','password4',27);
```
![圖片](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t3-1%E5%8A%A0%E5%85%A5test%20img.png)

- SELECT all rows from the member table.
```sql=
SELECT * FROM member;
```
![圖片](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t3-2%E9%81%B8%E5%8F%96%E5%85%A8%E9%83%A8%E7%9A%84%E5%88%97.png)

- SELECT all rows from the member table, in descending order of time.
```sql=
SELECT * FROM  ORDER BY time DESC;
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t3-3%E6%99%82%E9%96%93%E9%99%8D%E5%86%AA%E6%8E%92%E5%88%97.png)

- SELECT total 3 rows, second to fourth, from the member table, in descending order
of time.
```sql=
SELECT *  member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t3-4%E9%99%8D%E5%86%AA%E5%BE%8C%E9%81%B8%E5%8F%96.png)

- SELECT rows where username equals to test.
```sql=
SELECT * FROM member WHERE username='test';
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t3-5.png)
 
- SELECT rows where name includes the es keyword.
```sql=
SELECT * FROM member WHERE name LIKE '%es%';
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t3-6.png)


- SELECT rows where both username and password equal to test.
```sql=
 SELECT * FROM member WHERE username='test' AND password='test';
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t3-7.png)

- UPDATE data in name column to test2 where username equals to test.
```sql=
 UPDATE member SET name='test2'WHERE username='test';
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t3-8.png)
---
# Task 4

- SELECT how many rows from the member table.
```sql=
SELECT COUNT(*) FROM member;
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t4-1.png)

- SELECT the sum of follower_count of all the rows from the member table.
```sql=
SELECT SUM(follower_count) AS total_followers FROM member;
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t4-2.png)

- SELECT the average of follower_count of all the rows from the member table.
```sql=
SELECT AVG(follower_count) AS average_followers FROM member;
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t4-3.png)

- SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table.
```sql=
 SELECT AVG(follower_count) AS average_followers 
     FROM (
         SELECT follower_count 
         FROM member 
         ORDER BY follower_count DESC 
         LIMIT 2
     ) AS two_followers;
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t4-4.png)
---
# Task 5

- Create a new table named message, in the website database.
```sql=
CREATE TABLE message (
         id BIGINT PRIMARY KEY AUTO_INCREMENT,
         member_id BIGINT NOT NULL,
         content VARCHAR(255) NOT NULL,
         like_count INT UNSIGNED NOT NULL DEFAULT 0,
         time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
         CONSTRAINT fk_user_id FOREIGN KEY (member_id) REFERENCES member(id)
     );
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t5-1.png)
- SELECT all messages, including sender names. We have to JOIN the member table to get that.
```sql=
SELECT * FROM member INNER JOIN message ON member.id=message.member_id;
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t5-2.png)
- SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
- ```sql=
  SELECT message.*, member.name
     FROM message
     JOIN member ON message.member_id = member.id
     WHERE member.username = 'test';
  ```
  ![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t5-3.png)
  
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
```sql=
  SELECT AVG(message.like_count) AS average_like_count
     FROM message
     JOIN member ON message.member_id = member.id
     WHERE member.username = 'test';
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t5-4.png)
  
- Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
```sql=
SELECT member.username, AVG(message.like_count) AS average_like_count
     FROM message
     JOIN member ON message.member_id = member.id
     GROUP BY member.username;
```
![](https://github.com/yinxoxo/WeHelp.github.io/blob/main/week5/week5%20screenshot/t5-5.png)
