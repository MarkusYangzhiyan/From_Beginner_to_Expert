# MySQL 启停、连接与维护练习说明

本文记录本项目本地 MySQL 练习环境的启动、连接、建表、数据维护和权限验证流程。

## 1. 环境信息

```text
Docker 镜像：mysql:8.0
容器名称：agent-mysql
主机地址：127.0.0.1
主机端口：3307
容器端口：3306
数据卷：agent_mysql_data
练习数据库：products
```

`127.0.0.1` 表示只允许本机访问。数据库文件保存在 Docker 数据卷
`agent_mysql_data` 中，停止或重启容器不会清除数据。

## 2. MySQL 启停与检查

Docker Desktop 启动后，在 PowerShell 中执行以下命令。

```powershell
# 查看容器状态
docker ps -a --filter name=agent-mysql

# 启动容器
docker start agent-mysql

# 停止容器
docker stop agent-mysql

# 重启容器
docker restart agent-mysql

# 查看最近 100 行日志
docker logs --tail 100 agent-mysql
```

`docker run` 只用于首次创建容器。容器已经存在时，日常使用
`docker start agent-mysql` 即可。

## 3. 使用 DBeaver 连接

在 DBeaver 中新建 MySQL 连接，并填写：

```text
主机：127.0.0.1
端口：3307
数据库：可先留空，连接后选择 products
用户名：root、app_user 或 readonly_user
密码：填写对应的本地练习密码
```

如果出现 `Public Key Retrieval is not allowed`，在连接的驱动属性中设置：

```text
allowPublicKeyRetrieval=true
```

连接成功后执行：

```sql
SELECT DATABASE(), VERSION(), CURRENT_USER();
SHOW DATABASES;
```

其中：

- `root` 用于建库、建表和用户权限管理。
- `app_user` 用于业务数据的查询、新增、修改和删除。
- `readonly_user` 只用于查询。

## 4. 创建数据库和表

使用 `root` 连接，创建练习数据库：

```sql
CREATE DATABASE IF NOT EXISTS products
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE products;
```

首次初始化时，按照以下顺序执行项目中的 SQL 文件：

1. `database/categories_schema.sql`：创建商品分类表。
2. `database/products_schema.sql`：创建商品表及分类外键。
3. `database/seed.sql`：插入分类和商品样例数据。
4. `database/permission.sql`：创建用户并分配权限。

`products` 表依赖 `categories` 表，所以不能颠倒前两个建表脚本的顺序。

执行后检查：

```sql
USE products;
SHOW TABLES;
DESCRIBE categories;
DESCRIBE products;
SHOW CREATE TABLE products;
```

## 5. 数据查询练习

查询商品及其分类：

```sql
SELECT
    p.id,
    p.name,
    c.name AS category_name,
    p.price,
    p.stock
FROM products AS p
JOIN categories AS c ON c.id = p.category_id
ORDER BY p.id;
```

按分类和最高价格筛选：

```sql
SELECT
    p.id,
    p.name,
    c.name AS category_name,
    p.price,
    p.stock
FROM products AS p
JOIN categories AS c ON c.id = p.category_id
WHERE c.name = 'GPU'
  AND p.price <= 10000
ORDER BY p.price DESC;
```

## 6. 数据增删改练习

新增商品：

```sql
INSERT INTO products (
    name,
    category_id,
    price,
    stock,
    description
)
VALUES (
    'RTX-5090',
    1,
    19999.00,
    3,
    '权限和 CRUD 练习数据'
);
```

修改商品：

```sql
UPDATE products
SET price = 18999.00,
    stock = 5
WHERE name = 'RTX-5090';
```

删除商品：

```sql
DELETE FROM products
WHERE name = 'RTX-5090';
```

执行 `UPDATE` 或 `DELETE` 前，先用相同的 `WHERE` 条件执行 `SELECT`，确认影响范围：

```sql
SELECT *
FROM products
WHERE name = 'RTX-5090';
```

需要练习但不想保留数据时，可以使用事务：

```sql
START TRANSACTION;

UPDATE products
SET stock = stock + 1
WHERE id = 1;

SELECT * FROM products WHERE id = 1;

ROLLBACK;
```

- `COMMIT`：确认并永久保存本次事务的修改。
- `ROLLBACK`：撤销本次事务中尚未提交的修改。

## 7. 用户与权限管理

用户和权限定义保存在 `database/permission.sql`。修改用户权限必须使用
`root` 等具备用户管理权限的账号。

查看当前 MySQL 实例中的用户：

```sql
SELECT User, Host
FROM mysql.user
ORDER BY User, Host;
```

查看指定用户权限：

```sql
SHOW GRANTS FOR 'app_user'@'%';
SHOW GRANTS FOR 'readonly_user'@'%';
```

当前权限目标：

```text
app_user：对 products 数据库拥有 SELECT、INSERT、UPDATE、DELETE 权限
readonly_user：对 products 数据库只拥有 SELECT 权限
```

`'app_user'@'%'` 中，`app_user` 是用户名，`@` 用来分隔用户名和来源主机，
`%` 表示允许该用户从任意主机地址连接。由于 Docker 端口目前只绑定到
`127.0.0.1`，外部机器仍不能直接连接此数据库。

## 8. 权限验证

在 DBeaver 中分别建立 `app_user` 和 `readonly_user` 两个连接，不能只使用
`root` 模拟测试。

两个用户都应当可以执行：

```sql
SELECT COUNT(*) FROM products.products;
```

使用 `app_user` 执行以下事务，所有数据操作应成功，最后通过 `ROLLBACK`
撤销测试数据：

```sql
START TRANSACTION;

INSERT INTO products.categories (name, description)
VALUES ('PermissionTest', '权限测试临时分类');

SET @test_category_id = LAST_INSERT_ID();

UPDATE products.categories
SET description = '已通过 UPDATE 测试'
WHERE id = @test_category_id;

DELETE FROM products.categories
WHERE id = @test_category_id;

ROLLBACK;
```

使用 `readonly_user` 执行以下语句：

```sql
SELECT * FROM products.products LIMIT 5;

INSERT INTO products.categories (name, description)
VALUES ('ReadonlyTest', '该语句应该失败');

UPDATE products.products
SET stock = stock
WHERE id = 1;

DELETE FROM products.products
WHERE id = 0;
```

预期结果：`SELECT` 成功，`INSERT`、`UPDATE` 和 `DELETE` 均被 MySQL 拒绝。
即使 `WHERE` 没有匹配任何记录，MySQL 仍会先检查用户是否拥有相应权限。

## 9. 安全与日常使用约定

- 日常程序连接使用 `app_user`，不要使用 `root`。
- 报表、查看和只读场景使用 `readonly_user`。
- 不把生产密码或真实敏感信息提交到 Git。
- SQL 脚本保存为文件，不依赖 DBeaver 中尚未保存的编辑器标签页。
- 执行修改和删除前先查询影响范围，并确保 `WHERE` 条件正确。
- 停止容器不会删除数据；不要随意删除 `agent_mysql_data` 数据卷。

