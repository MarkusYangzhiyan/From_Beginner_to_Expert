# 第二周测试卷：Python 工程化、测试与 Git 协作

考试范围：Day 008-Day 014  
建议时间：90 分钟  
满分：100 分  
姓名：__________  日期：__________  得分：__________

## 答题说明

1. 本卷重点考察模块化、面向对象、类型提示、日志、测试、命令行和 Git。
2. 不要求编写完整程序，只需补关键语句、解释代码或写出操作命令。
3. 请直接在每道题的“答：”后填写答案。

## 一、基础选择题（共 20 分，每题 2 分）

### 1. Python 目录中加入 `__init__.py` 后，通常表示什么？（2 分）

A. 目录只能保存 JSON  
B. 目录可作为 Python 包导入  
C. 目录会自动成为虚拟环境  
D. 目录会自动运行所有脚本

答：

### 2. 从项目根目录运行包中的主模块，推荐使用哪个命令？（2 分）

A. `python product_app/main.py`  
B. `python -m product_app.main`  
C. `python -m main.product_app`  
D. `run product_app.main`

答：

### 3. `@dataclass` 最主要的作用是什么？（2 分）

A. 自动创建数据库表  
B. 为数据类自动生成常用方法，如 `__init__`  
C. 把函数变成类方法  
D. 自动捕获异常

答：

### 4. 使用 `@classmethod` 修饰的方法，第一个参数通常是什么？（2 分）

A. `self`  
B. `cls`  
C. `data`  
D. `args`

答：

### 5. `id: str | None` 表示什么？（2 分）

A. `id` 只能是空值  
B. `id` 可以是字符串，也可以是 `None`  
C. `id` 必须同时是字符串和空值  
D. `id` 是字符串列表

答：

### 6. 哪个场景最适合使用 `Enum`？（2 分）

A. 保存任意数量的商品  
B. 管理固定的菜单选项  
C. 读取 JSON 文件  
D. 创建临时目录

答：

### 7. `logger = logging.getLogger(__name__)` 的主要用途是什么？（2 分）

A. 立即配置所有日志输出格式  
B. 获取以当前模块名命名的日志器  
C. 删除日志文件  
D. 把所有 `print` 自动改成日志

答：

### 8. Pytest 默认会识别下面哪个函数为测试函数？（2 分）

A. `def check_filter():`  
B. `def filter_test():`  
C. `def test_filter_products():`  
D. `def run_filter():`

答：

### 9. Arrange-Act-Assert 中的 Act 表示什么？（2 分）

A. 准备测试数据  
B. 调用被测试的行为  
C. 验证结果  
D. 删除测试文件

答：

### 10. `git revert <commit>` 的特点是什么？（2 分）

A. 删除原提交及全部历史  
B. 创建一个与目标提交效果相反的新提交  
C. 只撤销工作区未提交内容  
D. 删除远程分支

答：

## 二、概念简答题（共 20 分，每题 4 分）

### 11. 当前 `product_app` 为什么要拆分为 `models.py`、`repository.py`、`service.py`、`cli.py` 和 `main.py`？分别写出其主要职责。（4 分）

答：

### 12. `Product.from_dict()` 为什么使用类方法，而 `product.to_dict()` 为什么使用对象方法？（4 分）

答：

### 13. 日志配置为什么通常放在程序入口，而不是在每个业务模块中重复调用 `basicConfig()`？（4 分）

答：

### 14. 什么是 Arrange-Act-Assert？请用商品筛选测试说明三个阶段分别做什么。（4 分）

答：

### 15. `argparse` 中 `required=True` 和 `type=positive_float` 分别负责什么？（4 分）

答：

## 三、代码阅读与关键代码题（共 40 分，每题 10 分）

### 16. 阅读数据模型转换代码。（10 分）

```python
@dataclass
class Product:
    id: str | None
    name: str
    price: float

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Product":
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            price=float(data.get("price", 0)),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }
```

回答：

1. `cls(...)` 最终创建的是什么？（2 分）
2. `data.get("name", "")` 中第二个参数的作用是什么？（2 分）
3. 为什么返回类型写成 `"Product"`？（3 分）
4. `self.name` 表示什么？（3 分）

答：

### 17. 阅读仓储层代码。（10 分）

```python
def load_products(file_path: Path) -> ProductList:
    try:
        text = file_path.read_text(encoding="utf-8")
        product_dicts = json.loads(text)
        return [Product.from_dict(item) for item in product_dicts]
    except FileNotFoundError:
        logger.error("Cannot find %r", file_path)
        return []
    except json.JSONDecodeError as error:
        logger.error("Cannot parse %r: %r", file_path, error)
        return []
```

回答：

1. 列表推导式最终返回什么结构？（3 分）
2. 两个异常分开捕获有什么价值？（2 分）
3. 第二条日志有几个 `%r`，后面为什么必须提供两个参数？（3 分）
4. `%r` 和 `%s` 的显示结果通常有什么区别？（2 分）

答：

### 18. 阅读 Pytest 测试。（10 分）

```python
def test_filter_products_by_name() -> None:
    # Arrange
    products = [
        Product(id="1", name="RTX-4090", category=["GPU"], price=9999),
        Product(id="2", name="Keyboard", category=["Peripheral"], price=500),
    ]

    # Act
    results = filter_products(products, name="4090")

    # Assert
    assert len(results) == 1
    assert results[0].name == "RTX-4090"
```

回答：

1. 指出 Arrange、Act、Assert 各自在验证什么。（4 分）
2. 这个函数会被 Pytest 识别为几个测试？为什么不是两个？（3 分）
3. 如果第二个断言失败，`1 passed` 还会出现吗？说明原因。（3 分）

答：

### 19. 阅读命令行解析代码。（10 分）

```python
search_parser.add_argument("--name", default="")
search_parser.add_argument("--category", default="")
search_parser.add_argument("--max-price", type=positive_float)

args = parser.parse_args([
    "search",
    "--name", "4090",
    "--max-price", "10000",
])
```

回答：

1. `args.name` 的值和类型是什么？（2 分）
2. `args.category` 的值是什么？（2 分）
3. `args.max_price` 的值和类型是什么？为什么不是字符串？（3 分）
4. 命令行参数写作 `--max-price`，为什么属性名通常是 `args.max_price`？（3 分）

答：

## 四、命令与协作流程题（共 20 分，每题 5 分）

### 20. 写出以下三条检查命令：编译检查三个模块、Ruff 检查包、运行全部 Pytest。（5 分）

答：

### 21. 从 `dev_yzy` 创建并切换到 `feature/search-help`，提交修改并首次推送远程分支。写出主要命令顺序。（5 分）

答：

### 22. PR 已在 GitHub 合并到远程 `dev_yzy`，本地仍停留在旧版本。写出切回 `dev_yzy` 并以 fast-forward 方式同步的命令。（5 分）

答：

### 23. 回答以下 Git 问题。（5 分）

1. 用什么命令查看当前分支与 `origin/dev_yzy` 的提交差异？（2 分）
2. 用什么命令安全撤销提交 `5c2d37a` 并保留历史？（2 分）
3. `git tag -a v0.1.0 -m "Product Manager CLI v0.1.0"` 标记的是哪个状态？（1 分）

答：

## 阅卷区

选择题：____ / 20  
概念题：____ / 20  
代码题：____ / 40  
操作题：____ / 20  
总分：____ / 100

