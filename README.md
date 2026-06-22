# From_Beginner_to_Expert

6 个月 AI-Agent 工程师成长计划实践仓库。

## 当前项目：Product Manager CLI

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
   [--init--.py](product_app/__init__.py)、[requirements.txt](requirements.txt)。
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
