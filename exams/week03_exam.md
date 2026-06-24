# 第三周测试卷：Docker MySQL、SQL 与权限管理

考试范围：Day 015-Day 021  
建议时间：90 分钟  
满分：100 分  
姓名：__________  日期：__________  得分：__________

## 答题说明

1. 本卷以当前 Docker MySQL 和 DBeaver 练习环境为背景。
2. 不要求创建完整数据库，只需解释概念、阅读 SQL、写关键命令或判断结果。
3. 请直接在每道题的“答：”后填写答案。

## 一、基础选择题（共 20 分，每题 2 分）

### 1. Docker 镜像与容器的关系，正确的是哪一项？（2 分）

A. 镜像是运行中的数据库进程，容器是安装包  
B. 镜像是创建容器的模板，容器是镜像的运行实例  
C. 镜像和容器完全相同  
D. 一个镜像只能创建一个容器

答：

### 2. `127.0.0.1:3307:3306` 表示什么？（2 分）

A. 宿主机 3306 映射到容器 3307  
B. 宿主机 3307 映射到容器 3306，并只绑定本机地址  
C. 两个 MySQL 数据库名称  
D. 用户名和密码

答：

### 3. Docker 数据卷 `agent_mysql_data` 的主要作用是什么？（2 分）

A. 保存 DBeaver 安装程序  
B. 持久化 MySQL 数据，使容器停止后数据仍保留  
C. 自动生成 SQL 查询  
D. 保存 Git 分支

答：

### 4. 在 MySQL 中，Schema 与 Database 通常是什么关系？（2 分）

A. 完全无关  
B. 在 MySQL 中通常可以视为同义概念  
C. Schema 一定是表  
D. Database 一定是用户

答：

### 5. 表中的主键 `PRIMARY KEY` 主要用于什么？（2 分）

A. 允许每行重复  
B. 唯一标识一条记录  
C. 保存长文本  
D. 允许字段为空

答：

### 6. `NOT NULL` 约束表示什么？（2 分）

A. 字段不能存储 `NULL`  
B. 字段不能存储数字  
C. 字段必须唯一  
D. 字段自动递增

答：

### 7. `products.category_id` 引用 `categories.id`，这是什么关系？（2 分）

A. 商品表的主键引用自己  
B. 商品表通过外键关联分类表  
C. 两张表没有关系  
D. 分类名称必须等于商品名称

答：

### 8. 没有执行 `COMMIT` 时，`ROLLBACK` 的作用是什么？（2 分）

A. 永久保存修改  
B. 撤销当前事务中尚未提交的修改  
C. 删除数据库  
D. 重启容器

答：

### 9. MySQL 账号 `'readonly_user'@'%'` 中的 `%` 表示什么？（2 分）

A. 密码为空  
B. 允许从任意来源主机连接  
C. 拥有所有权限  
D. 只能从 localhost 连接

答：

### 10. `GRANT USAGE ON *.* TO 'app_user'@'%'` 通常表示什么？（2 分）

A. 用户拥有所有数据库的所有权限  
B. 账号存在，但没有额外的全局业务权限  
C. 用户可以删除所有数据库  
D. 用户只能修改表结构

答：

## 二、概念简答题（共 20 分，每题 4 分）

### 11. 说明 MySQL 服务器、数据库、表、行和字段之间的层级关系。（4 分）

答：

### 12. 分别解释主键、外键、唯一约束和默认值，并各说明一个当前商品数据库中的用途。（4 分）

答：

### 13. `schema.sql`、`seed.sql` 和 `permission.sql` 分别应该保存什么内容？为什么要把它们保存为文件？（4 分）

答：

### 14. 关系图中 `categories` 与 `products` 为什么是一对多关系？请举例说明。（4 分）

答：

### 15. 什么是“最小权限原则”？为什么 Python 业务程序不应该直接使用 `root` 账号？（4 分）

答：

## 三、SQL 阅读与关键语句题（共 40 分，每题 10 分）

### 16. 阅读建表语句。（10 分）

```sql
CREATE TABLE products (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    category_id BIGINT UNSIGNED NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    stock INT UNSIGNED NOT NULL DEFAULT 0,
    PRIMARY KEY (id),
    CONSTRAINT fk_products_category
        FOREIGN KEY (category_id)
        REFERENCES categories (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
```

回答：

1. `AUTO_INCREMENT` 有什么作用？（2 分）
2. `DECIMAL(12, 2)` 大致表示什么？为什么价格适合使用它？（3 分）
3. `DEFAULT 0` 在什么情况下生效？（2 分）
4. `ON DELETE RESTRICT` 和 `ON UPDATE CASCADE` 分别表示什么？（3 分）

答：

### 17. 阅读数据维护语句。（10 分）

```sql
SELECT * FROM products WHERE id = 10;

UPDATE products
SET price = 9999.00,
    stock = 8
WHERE id = 10;

DELETE FROM products
WHERE id = 10;
```

回答：

1. 为什么修改或删除前先执行第一条 `SELECT`？（3 分）
2. 如果省略 `UPDATE` 的 `WHERE`，可能产生什么结果？（3 分）
3. 如果商品 `id=10` 不存在，`DELETE` 会删除多少行？（2 分）
4. 写出查询价格不超过 10000 且库存大于 0 的商品所需的 `WHERE` 条件。（2 分）

答：

### 18. 阅读事务代码。（10 分）

```sql
START TRANSACTION;

UPDATE products
SET stock = stock - 1
WHERE id = 1;

SELECT stock FROM products WHERE id = 1;

ROLLBACK;
```

回答：

1. 事务中间的 `SELECT` 可能看到修改后的库存吗？（2 分）
2. 执行 `ROLLBACK` 后库存最终是否改变？（3 分）
3. 如果把 `ROLLBACK` 改为 `COMMIT`，结果有什么不同？（3 分）
4. 使用事务做练习有什么好处？（2 分）

答：

### 19. 阅读权限语句。（10 分）

```sql
REVOKE ALL PRIVILEGES, GRANT OPTION
FROM 'readonly_user'@'%';

GRANT SELECT
ON products.*
TO 'readonly_user'@'%';

SHOW GRANTS FOR 'readonly_user'@'%';
```

回答：

1. 第一条语句撤销了什么？账号本身是否因此删除？（3 分）
2. `products.*` 中两个部分分别代表什么？（2 分）
3. 授权后，该用户能否执行 `INSERT`？为什么？（2 分）
4. 最后一条语句用于做什么？（3 分）

答：

## 四、命令与实际操作题（共 20 分，每题 5 分）

### 20. 写出查看 `agent-mysql` 容器状态、启动、停止和查看最近日志的 Docker 命令。（5 分）

答：

### 21. 写出当前 DBeaver 连接 Docker MySQL 所需的主机和端口，并解释为什么 DBeaver 不能填写容器内部端口作为宿主机端口。（5 分）

答：

### 22. 使用 `root` 查看所有 MySQL 用户，并查看 `app_user` 当前授权，各写一条 SQL。（5 分）

答：

### 23. 设计一个最小权限验证流程，证明 `readonly_user` 可以查询，但不能新增、修改和删除。需要写出连接方式和至少四条测试 SQL 的目的，不要求填写真实密码。（5 分）

答：

## 阅卷区

选择题：____ / 20  
概念题：____ / 20  
SQL 题：____ / 40  
操作题：____ / 20  
总分：____ / 100

