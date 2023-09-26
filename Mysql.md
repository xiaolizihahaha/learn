# Mysql（密码xiaolizi）

## 1.安装

1. 安装Mysql

   ```
   官网下载 arm架构的
   ```

2. 启动Mysql

   ```
   设置->开启mysql服务
   ```

3. 查看版本

   ```
   mysql --version
   ```

4. 修改密码

   ```
   mysqladmin -u root password "new_password"
   ```

5. 安装目录

   ```
   /usr/local/mysql/bin/mysql
   ```

   

## 2.使用

1. 进入mysql

   ```
   mysql -u root -p 
   ```

2. 退出mysql

   ```
   exit
   ```

3. 进入数据库

   ```
   use 数据库名
   ```

   

4. 查看用户信息

   ```
   use mysql;
   SELECT user FROM mysql.user
   ```

5. 显示数据库的端口号（3306）

   ```
   show global variables like 'port';  
   ```


## 3.基本使用

1. 查看表

   ```
   show tables;
   
   SELECT * FROM 表名   //表中记录
   
   describe 表名   //表结构
   ```

   

2. 创建表

   ```
   CREATE TABLE user_test(
   id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '用户id',
   username varchar(50) NOT NULL COMMENT '用户姓名',
   password varchar(50) NOT NULL COMMENT '用户手机号',
   PRIMARY KEY (id) USING BTREE
   )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
   
   ```

3. 增加数据

   ```
   insert into user_test(username,password) values("Mary","19107120261");
   ```

4. 删除表

   ```
   DROP TABLE 表名
   ```

5. 