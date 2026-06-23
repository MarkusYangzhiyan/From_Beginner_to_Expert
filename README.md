# From_Beginner_to_Expert

6 个月 AI-Agent 工程师成长计划实践仓库。

## Python 工程化、测试与 Git 练习：Product Manager CLI

Product Manager CLI 是一个基于 Python 的商品数据管理命令行程序，目前支持：

- 从 JSON 文件加载和保存商品数据。
- 按商品名称、分类和最高价格进行筛选。
- 按价格对商品进行排序。
- 接收并校验用户输入的新商品信息。
- 将新商品添加到商品列表并保存。
- 使用日志记录加载失败、查询结果和商品添加操作。
- 使用 Pytest 测试查询、排序和异常处理。

## 模块化结构

```text
product_app/
|-- __init__.py    # Python 包标识
|-- models.py      # Product 数据模型
|-- repository.py  # JSON 数据读取和保存
|-- service.py     # 查询、排序和添加业务逻辑
|-- cli.py         # 菜单、输入校验和结果显示
`-- main.py        # 组合各模块并启动程序
```

## 环境要求

- Python 3.12
- Git
- Docker Desktop
- DBeaver
- Windows PowerShell

## 安装

克隆当前开发分支并进入项目目录：

```powershell
git clone --branch dev_yzy https://github.com/MarkusYangzhiyan/From_Beginner_to_Expert.git
cd From_Beginner_to_Expert
```

创建并激活虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

安装项目依赖：

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 运行

以下命令需要在项目根目录执行。

### 交互模式

```powershell
python -m product_app.main
```

程序启动后，可以通过菜单查询商品、添加商品或退出程序。

### 命令行查询

```powershell
python -m product_app.main search --name 4090 --category GPU --max-price 10000
```

查询参数可以按需省略，例如只按名称查询：

```powershell
python -m product_app.main search --name 4090
```

### 命令行添加商品

```powershell
python -m product_app.main add --name RTX-5090 --category GPU --price 15999
```

添加商品会修改 `data/processed/products.json`。名称和分类不能为空，价格必须是大于 0 的数字。

## 本地 MySQL 数据库

项目使用 Docker 运行本地 MySQL 8.0，并通过 DBeaver 管理。由于本机已有其他 MySQL 服务占用 `3306`，Docker 容器使用本机端口 `3307`。

### 数据库配置

```text
Docker 镜像：mysql:8.0
容器名称：agent-mysql
主机地址：127.0.0.1
主机端口：3307
容器端口：3306
数据卷：agent_mysql_data
数据库：agent_learning
```

`127.0.0.1` 表示数据库只接受本机连接。数据保存在 `agent_mysql_data` 数据卷中，停止或重启容器不会删除数据。

### 首次创建容器

下面的命令只在首次创建容器时执行：

```powershell
docker run --name agent-mysql `
  --restart unless-stopped `
  -e MYSQL_ALLOW_EMPTY_PASSWORD=yes `
  -e MYSQL_ROOT_HOST=% `
  -p 127.0.0.1:3307:3306 `
  -v agent_mysql_data:/var/lib/mysql `
  -d mysql:8.0 `
  --default-authentication-plugin=mysql_native_password
```

当前 root 空密码配置仅用于绑定在 `127.0.0.1` 的本地学习环境，禁止用于共享、测试或生产服务器。

### 常用 Docker 命令

```powershell
# 查看运行状态
docker ps --filter name=agent-mysql

# 查看日志
docker logs agent-mysql

# 停止、启动和重启
docker stop agent-mysql
docker start agent-mysql
docker restart agent-mysql
```

容器已经创建后，继续使用时执行 `docker start agent-mysql`，不需要重复执行 `docker run`。

### DBeaver 连接

DBeaver 中已配置连接 `Agent MySQL Docker`，连接参数如下：

```text
主机：127.0.0.1
端口：3307
数据库：可留空，或填写 agent_learning
用户名：root
密码：留空
```

连接后可运行以下 SQL 验证：

```sql
SHOW DATABASES;
USE agent_learning;
SELECT DATABASE(), VERSION();
```

### Python 连接

Python 程序使用 `app_user` 连接 `agent_learning`，不要使用 root。先安装驱动：

```powershell
python -m pip install mysql-connector-python
```

在本地 `.env` 中配置，不要将真实密码提交到 Git：

```dotenv
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3307
MYSQL_DATABASE=agent_learning
MYSQL_USER=app_user
MYSQL_PASSWORD=<LOCAL_PASSWORD>
```

连接示例：

```python
import os

import mysql.connector


connection = mysql.connector.connect(
    host=os.environ["MYSQL_HOST"],
    port=int(os.environ["MYSQL_PORT"]),
    database=os.environ["MYSQL_DATABASE"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
)

try:
    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE(), VERSION()")
    print(cursor.fetchone())
finally:
    cursor.close()
    connection.close()
```

当前 `app_user` 具有 `agent_learning` 下建表和数据增删改查权限。后续权限练习将另外创建只读用户。

## 测试与代码检查

运行全部自动化测试：

```powershell
python -m pytest -q
```

当前预期结果：

```text
12 passed
```

运行 Ruff 代码检查：

```powershell
python -m ruff check product_app tests
```

当前预期结果：

```text
All checks passed!
```

## 第一周主要成果和进度

1. **开发环境与版本控制：**
   Python 3.12、VS Code、Git操作、Docker Desktop、DBeaver。
   [开发环境检查.md](开发环境检查.md)、[.gitignore](.gitignore)。
2. **商品查询原型：**
   商品列表、名称筛选、分类筛选、最高价格筛选、组合查询、输入校验。
   [products.py](products.py)、[product_filter.py](product_filter.py)、[product_search_and_add.py](product_search_and_add.py)。
3. **文件与数据处理：**
   文件读写、`pathlib`、JSON、gzip、All Beauty 真实商品数据、数据提取与保存。
   [raw_data_process.py](raw_data_process.py)、[product_search_and_add.py](product_search_and_add.py)、[products.json](data/processed/products.json)。
4. **异常处理与调试：**
   `try`、`except`、文件不存在、JSON 格式错误、VS Code 断点调试、函数拆分。
   [raw_data_process.py](raw_data_process.py)、[product_search_and_add.py](product_search_and_add.py)。

## 第二周主要成果和进度

1. **Python 包与工程环境：**
   `product_app`、虚拟环境、依赖管理。
   [__init__.py](product_app/__init__.py)、[requirements.txt](requirements.txt)。
2. **数据模型与类型提示：**
   类、对象、`dataclass`、`Product`、`from_dict()`、`to_dict()`、类型提示、`Enum`。
   [models.py](product_app/models.py)、[cli.py](product_app/cli.py)、[service.py](product_app/service.py)。
3. **日志与代码质量：**
   `logging`、终端日志、文件日志、日志级别、Ruff 代码检查。
   [main.py](product_app/main.py)、[cli.py](product_app/cli.py)、[repository.py](product_app/repository.py)、[service.py](product_app/service.py)、[requirements.txt](requirements.txt)。
4. **自动化测试：**
   Pytest、Arrange-Act-Assert、查询测试、排序测试、异常测试、命令行参数测试、12 个测试通过。
   [test_service.py](tests/test_service.py)。
5. **模块化重构：**
   数据模型、数据读写、业务逻辑、用户交互、程序入口、职责分离、单向依赖、解除循环导入。
   [models.py](product_app/models.py)、[repository.py](product_app/repository.py)、[service.py](product_app/service.py)、[cli.py](product_app/cli.py)、[main.py](product_app/main.py)。
6. **Git 分支与团队协作：**
   分支创建与切换、提交与推送、代码差异查看、本地合并、远程功能分支、Pull Request、代码 Review、PR 合并、本地同步、`git revert` 回退单个提交。
   [git_practice.md](git_practice.md)。

## 当前验证结果

- 所有 `product_app` 模块均可正常导入。
- 商品添加、JSON 保存和重新加载流程验证通过。
- Pytest：12 个测试全部通过。
- Ruff：检查全部通过。
