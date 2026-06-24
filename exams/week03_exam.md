# 第三周测试卷：Docker MySQL、SQL 与权限管理

## 批阅结果

**最终得分：48 / 100****成绩评价：暂未合格。数据库基础操作做过，但表约束、事务和 SOP 调用能力尚未形成稳定理解。**

> 第 20-23 题允许查阅自己编写的 SOP，但仍需要写出答案。记录过 SOP 是很好的工程习惯，
> 但“当我全对”不能证明能够找到并正确执行命令，因此这四题本次不计分。

### 分项成绩

| 部分             |         得分 |          满分 |
| ---------------- | -----------: | ------------: |
| 基础选择题       |           16 |            20 |
| 概念简答题       |           15 |            20 |
| SQL 阅读题       |           17 |            40 |
| 命令与实际操作题 |            0 |            20 |
| **总分**   | **48** | **100** |

### 逐题得分

| 题号 | 得分 | 满分 | 批阅说明                                                                                                 |
| ---- | ---: | ---: | -------------------------------------------------------------------------------------------------------- |
| 1    |    0 |    2 | 镜像是模板，容器是镜像的运行实例，正确答案是 B。                                                         |
| 2-5  |    8 |    8 | 全部正确。                                                                                               |
| 6    |    0 |    2 | `NOT NULL` 表示字段不能存储 `NULL`，正确答案是 A。                                                   |
| 7-10 |    8 |    8 | 全部正确。                                                                                               |
| 11   |    3 |    4 | 顺序基本正确；严格层级是服务器包含数据库，数据库包含表，表由字段定义并保存多行数据。DBeaver 只是客户端。 |
| 12   |    3 |    4 | 主键、外键和默认值基本正确；缺少唯一约束：指定列或列组合的值不能重复。                                   |
| 13   |    4 |    4 | 三类 SQL 文件的职责和保存价值说明正确。                                                                  |
| 14   |    3 |    4 | 一对多和例子正确；在这段关系中通常称 `categories` 为父表，`products` 为子表。                        |
| 15   |    2 |    4 | 知道不应滥用 root；还应明确每个账号只授予完成工作所必需的最少权限，以减少误操作和攻击影响。              |
| 16   |    0 |   10 | 未作答，需要复习自动递增、精确小数、默认值和外键动作。                                                   |
| 17   |    8 |   10 | `WHERE` 和组合条件掌握较好；无匹配记录时 `DELETE` 成功执行并影响 0 行，通常不会报错。                |
| 18   |    0 |   10 | 未作答，需要复习事务中的可见性、`COMMIT` 和 `ROLLBACK`。                                             |
| 19   |    9 |   10 | 权限范围理解较好；`REVOKE` 不会删除或修改密码，只撤销权限及授权能力。                                  |
| 20   |    0 |    5 | 未写出命令，无法验证。允许查阅 SOP 后补答。                                                              |
| 21   |    0 |    5 | 未写出连接信息和解释，无法验证。                                                                         |
| 22   |    0 |    5 | 未写出 SQL，无法验证。                                                                                   |
| 23   |    0 |    5 | 未写出验证流程，无法验证。                                                                               |

### 重点订正

1. 镜像与容器：镜像是只读模板，容器是由镜像创建的运行实例。同一个镜像可以创建多个容器。
2. 常见建表定义：

   - `AUTO_INCREMENT`：插入新记录时自动生成递增编号。
   - `DECIMAL(12, 2)`：最多 12 位有效数字，其中 2 位是小数，适合精确存储金额。
   - `DEFAULT 0`：插入记录时省略该字段，就使用默认值 `0`。
   - `ON DELETE RESTRICT`：存在关联商品时拒绝删除分类。
   - `ON UPDATE CASCADE`：分类主键更新时，关联商品的外键同步更新。
3. 事务题的结果：

   - 当前事务中的 `SELECT` 可以看到自己刚执行的 `UPDATE`。
   - `ROLLBACK` 会撤销尚未提交的库存修改。
   - `COMMIT` 会永久保存库存修改。
   - 练习时使用事务，可以验证操作后再决定提交或撤销。
4. Docker 常用命令：

   ```powershell
   docker ps -a --filter name=agent-mysql
   docker start agent-mysql
   docker stop agent-mysql
   docker logs --tail 100 agent-mysql
   ```
5. 当前 DBeaver 连接参数：

   ```text
   主机：127.0.0.1
   宿主机端口：3307
   容器内部端口：3306
   ```

   DBeaver 运行在宿主机上，所以连接 Docker 发布出来的 `3307`；`3306` 是容器内部端口。
6. 查看用户和授权：

   ```sql
   SELECT User, Host
   FROM mysql.user
   ORDER BY User, Host;

   SHOW GRANTS FOR 'app_user'@'%';
   ```
7. 使用独立的 `readonly_user` DBeaver 连接验证最小权限：

   ```sql
   SELECT * FROM products.products LIMIT 5;

   INSERT INTO products.categories (name)
   VALUES ('ReadonlyTest');

   UPDATE products.products
   SET stock = stock
   WHERE id = 1;

   DELETE FROM products.products
   WHERE id = 0;
   ```

   预期结果是 `SELECT` 成功，其余三条语句均因权限不足而失败。

考试范围：Day 015-Day 021
建议时间：90 分钟
满分：100 分
姓名：_____Markus_____  日期：_____2026-6-24_____  得分：__48 / 100__

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

答：a

### 2. `127.0.0.1:3307:3306` 表示什么？（2 分）

A. 宿主机 3306 映射到容器 3307
B. 宿主机 3307 映射到容器 3306，并只绑定本机地址
C. 两个 MySQL 数据库名称
D. 用户名和密码

答：b

### 3. Docker 数据卷 `agent_mysql_data` 的主要作用是什么？（2 分）

A. 保存 DBeaver 安装程序
B. 持久化 MySQL 数据，使容器停止后数据仍保留
C. 自动生成 SQL 查询
D. 保存 Git 分支

答：b

### 4. 在 MySQL 中，Schema 与 Database 通常是什么关系？（2 分）

A. 完全无关
B. 在 MySQL 中通常可以视为同义概念
C. Schema 一定是表
D. Database 一定是用户

答：b

### 5. 表中的主键 `PRIMARY KEY` 主要用于什么？（2 分）

A. 允许每行重复
B. 唯一标识一条记录
C. 保存长文本
D. 允许字段为空

答：b

### 6. `NOT NULL` 约束表示什么？（2 分）

A. 字段不能存储 `NULL`
B. 字段不能存储数字
C. 字段必须唯一
D. 字段自动递增

答：c

### 7. `products.category_id` 引用 `categories.id`，这是什么关系？（2 分）

A. 商品表的主键引用自己
B. 商品表通过外键关联分类表
C. 两张表没有关系
D. 分类名称必须等于商品名称

答：b

### 8. 没有执行 `COMMIT` 时，`ROLLBACK` 的作用是什么？（2 分）

A. 永久保存修改
B. 撤销当前事务中尚未提交的修改
C. 删除数据库
D. 重启容器

答：b

### 9. MySQL 账号 `'readonly_user'@'%'` 中的 `%` 表示什么？（2 分）

A. 密码为空
B. 允许从任意来源主机连接
C. 拥有所有权限
D. 只能从 localhost 连接

答：b

### 10. `GRANT USAGE ON *.* TO 'app_user'@'%'` 通常表示什么？（2 分）

A. 用户拥有所有数据库的所有权限
B. 账号存在，但没有额外的全局业务权限
C. 用户可以删除所有数据库
D. 用户只能修改表结构

答：b

## 二、概念简答题（共 20 分，每题 4 分）

### 11. 说明 MySQL 服务器、数据库、表、行和字段之间的层级关系。（4 分）

答：

1. 服务器启动 -- 通过DBeaver连接数据库 -- 在数据库中建立表 -- 表中有行和字段

### 12. 分别解释主键、外键、唯一约束和默认值，并各说明一个当前商品数据库中的用途。（4 分）

答：

1. 主键是唯一的，一条记录有一个主键
2. 外键是当前表和其他表连接的一个键
3. 唯一约束不知道
4. 默认值是如果不传这个参数的话，默认给什么

### 13. `schema.sql`、`seed.sql` 和 `permission.sql` 分别应该保存什么内容？为什么要把它们保存为文件？（4 分）

答：

1. schema保存数据库创建的内容，有哪些字段或者列，类型和默认值是什么等等
2. seed存的是样例数据的写入
3. permission存的是用户泉下按管理
4. 保存成文件是避免sql中语句丢失了，可复现，可查询

### 14. 关系图中 `categories` 与 `products` 为什么是一对多关系？请举例说明。（4 分）

答：

1. products是主表，通过category_id 和categories.id主键相连
2. 一个类别下可能会有多个产品，所以是一对多，比如说GPU类型下可能会有4090 ，5090等

### 15. 什么是“最小权限原则”？为什么 Python 业务程序不应该直接使用 `root` 账号？（4 分）

答：

1. root是管理者的，如果随便给开发人员用户权限的话，那么数据库的增删查改维护就比较混乱了

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

1. 不知道
2. 不知道
3. 不知道
4. 不知道

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

1. 方便删除修改后对比查看
2. 所有的行都会修改price和stock
3. 不存的话，不会删除，会报错
4. where price <= 10000 and stock >0;

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

答：这道题不会做

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

1. 此时用户存在，已经设置了密码，这个语句是把密码删除，权限撤销，不会删除账号
2. products是数据库，*代表这个数据库下所有的表
3. 不能，因为用户的权限只有select
4. 看一下readonly_user有哪些权限

## 四、命令与实际操作题（共 20 分，每题 5 分）

### 20. 写出查看 `agent-mysql` 容器状态、启动、停止和查看最近日志的 Docker 命令。（5 分）

答：这个题目当我全对，因为我记录下了SOP，不必背出来

### 21. 写出当前 DBeaver 连接 Docker MySQL 所需的主机和端口，并解释为什么 DBeaver 不能填写容器内部端口作为宿主机端口。（5 分）

答：这道题当我全对，因为我记录下了SOP，不必背出来

### 22. 使用 `root` 查看所有 MySQL 用户，并查看 `app_user` 当前授权，各写一条 SQL。（5 分）

答：这道题当我全对，因为我记录下了SOP，不必背出来

### 23. 设计一个最小权限验证流程，证明 `readonly_user` 可以查询，但不能新增、修改和删除。需要写出连接方式和至少四条测试 SQL 的目的，不要求填写真实密码。（5 分）

答：这道题当我全对，因为我记录下了SOP，不必背出来

## 阅卷区

选择题：16 / 20
概念题：15 / 20
SQL 题：17 / 40
操作题：0 / 20
总分：48 / 100
