# 第二周测试卷：Python 工程化、测试与 Git 协作

## 批阅结果

**最终得分：75 / 100**
**成绩评价：良好，Python 工程化概念掌握较稳，Git 命令准确性需要重点加强。**

### 分项成绩

| 部分             |         得分 |          满分 |
| ---------------- | -----------: | ------------: |
| 基础选择题       |           18 |            20 |
| 概念简答题       |           18 |            20 |
| 代码阅读题       |           32 |            40 |
| 命令与协作流程题 |            7 |            20 |
| **总分**   | **75** | **100** |

### 逐题得分

| 题号 | 得分 | 满分 | 批阅说明                                                                                                                                |
| ---- | ---: | ---: | --------------------------------------------------------------------------------------------------------------------------------------- |
| 1-3  |    6 |    6 | 全部正确。                                                                                                                              |
| 4    |    0 |    2 | 类方法的第一个参数通常是 `cls`，`self` 是对象方法的第一个参数。                                                                     |
| 5-10 |   12 |   12 | 全部正确。                                                                                                                              |
| 11   |    4 |    4 | 模块职责划分完整、准确。                                                                                                                |
| 12   |    4 |    4 | 已理解从字典创建对象和把对象转换为字典的方向。                                                                                          |
| 13   |    3 |    4 | 核心正确；集中配置还可以避免重复添加处理器、重复日志和格式不一致。                                                                      |
| 14   |    4 |    4 | AAA 三个阶段说明正确。                                                                                                                  |
| 15   |    3 |    4 | `required` 理解正确；`type` 会调用指定函数完成转换和校验，不只是描述格式。                                                          |
| 16   |    9 |   10 | 整体正确；`dict.get()` 的默认值在键不存在时使用，不是值为 `None` 或空字符串时使用。                                                 |
| 17   |    4 |   10 | 返回值应为 `list[Product]`；第二条日志有两个 `%r`，对应 `file_path` 和 `error`；`%r` 使用 `repr()`，`%s` 使用 `str()`。 |
| 18   |   10 |   10 | 对 AAA、测试函数数量和断言失败的理解全部正确。                                                                                          |
| 19   |    9 |   10 | 值和类型正确；还应明确 `positive_float` 被调用后把字符串转换成 `float`。                                                            |
| 20   |    3 |    5 | Ruff 和 Pytest 命令正确，但第一条应使用 `py_compile`，不是再次运行 Ruff。                                                             |
| 21   |    2 |    5 | 缺少创建分支的 `-c`，首次推送还应设置远程跟踪分支。                                                                                   |
| 22   |    1 |    5 | 知道需要 `pull`，但参数拼写和完整流程错误，应先切换分支再使用 `--ff-only`。                                                         |
| 23   |    1 |    5 | 标签理解基本正确；查看远程差异和安全回退提交的命令错误。                                                                                |

### 重点订正

1. 类方法与对象方法：

   ```python
   @classmethod
   def from_dict(cls, data):
       ...

   def to_dict(self):
       ...
   ```
2. `ProductList` 是 `list[Product]`，不是 `list[dict[str, Any]]`。字典经过
   `Product.from_dict()` 后已经变成 `Product` 对象。
3. 日志中两个 `%r` 必须对应两个参数：

   ```python
   logger.error("Cannot parse %r: %r", file_path, error)
   ```

   `%r` 通常显示适合调试的 `repr()` 结果，`%s` 通常显示面向用户的 `str()` 结果。
4. 正确的检查命令示例：

   ```powershell
   python -m py_compile product_app\models.py product_app\service.py product_app\cli.py
   python -m ruff check product_app
   python -m pytest -q
   ```
5. 创建、提交并首次推送功能分支：

   ```powershell
   git switch dev_yzy
   git switch -c feature/search-help
   git add .
   git commit -m "feat: add search help"
   git push -u origin feature/search-help
   ```
6. PR 合并后同步本地主分支：

   ```powershell
   git switch dev_yzy
   git pull --ff-only origin dev_yzy
   ```
7. 查看差异与安全撤销提交：

   ```powershell
   git log --oneline --left-right HEAD...origin/dev_yzy
   git diff HEAD..origin/dev_yzy
   git revert --no-edit 5c2d37a
   ```
8. 带注释标签默认标记当前检出的提交，也就是当前 `HEAD` 对应的仓库快照。

考试范围：Day 008-Day 014
建议时间：90 分钟
满分：100 分
姓名：_____Markus_____  日期：___2026-6-24_______  得分：__75 / 100__

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

答：b

### 2. 从项目根目录运行包中的主模块，推荐使用哪个命令？（2 分）

A. `python product_app/main.py`
B. `python -m product_app.main`
C. `python -m main.product_app`
D. `run product_app.main`

答：b

### 3. `@dataclass` 最主要的作用是什么？（2 分）

A. 自动创建数据库表
B. 为数据类自动生成常用方法，如 `__init__`
C. 把函数变成类方法
D. 自动捕获异常

答：b

### 4. 使用 `@classmethod` 修饰的方法，第一个参数通常是什么？（2 分）

A. `self`
B. `cls`
C. `data`
D. `args`

答：b

### 5. `id: str | None` 表示什么？（2 分）

A. `id` 只能是空值
B. `id` 可以是字符串，也可以是 `None`
C. `id` 必须同时是字符串和空值
D. `id` 是字符串列表

答：b

### 6. 哪个场景最适合使用 `Enum`？（2 分）

A. 保存任意数量的商品
B. 管理固定的菜单选项
C. 读取 JSON 文件
D. 创建临时目录

答：b

### 7. `logger = logging.getLogger(__name__)` 的主要用途是什么？（2 分）

A. 立即配置所有日志输出格式
B. 获取以当前模块名命名的日志器
C. 删除日志文件
D. 把所有 `print` 自动改成日志

答：b

### 8. Pytest 默认会识别下面哪个函数为测试函数？（2 分）

A. `def check_filter():`
B. `def filter_test():`
C. `def test_filter_products():`
D. `def run_filter():`

答：c

### 9. Arrange-Act-Assert 中的 Act 表示什么？（2 分）

A. 准备测试数据
B. 调用被测试的行为
C. 验证结果
D. 删除测试文件

答：b

### 10. `git revert <commit>` 的特点是什么？（2 分）

A. 删除原提交及全部历史
B. 创建一个与目标提交效果相反的新提交
C. 只撤销工作区未提交内容
D. 删除远程分支

答：b

## 二、概念简答题（共 20 分，每题 4 分）

### 11. 当前 `product_app` 为什么要拆分为 `models.py`、`repository.py`、`service.py`、`cli.py` 和 `main.py`？分别写出其主要职责。（4 分）

答：

1. 目的是为了让不同的功能解耦，方便阅读和管理
2. models.py  定义了Product和ProductList的类
3. repository.py 主要功能是做products数据的读取和保存
4. service.py 主要放的是业务功能函数，比如说filter函数
5. cli.py 主要放的是交互功能的函数 ，需要用户input的函数都存在这里，比如说get_new_product函数等
6. main.py 是主程序入口

### 12. `Product.from_dict()` 为什么使用类方法，而 `product.to_dict()` 为什么使用对象方法？（4 分）

答：

1. `Product.from_dict()`使用类方法是因为这个函数是需要把json中的products变成python的类
2. `product.to_dict()`使用对象方法是因为这个函数是需要把python的product类变成一个dict对象存回json中

### 13. 日志配置为什么通常放在程序入口，而不是在每个业务模块中重复调用 `basicConfig()`？（4 分）

答：

1. 在程序入口一次配置，全部的业务模块都可以使用，因为main主程序入口配置后，后面会把业务模块串起来的。

### 14. 什么是 Arrange-Act-Assert？请用商品筛选测试说明三个阶段分别做什么。（4 分）

答：

1. AAA就是一种pytest测试代码的方式
2. arrange先准备数据，比如说load_products() 先生成数据，然后act是执行需要测试的函数，比如说filter_product_by_name，然后用assert来判断我们预期的结果和本次测试的结果是否相同

### 15. `argparse` 中 `required=True` 和 `type=positive_float` 分别负责什么？（4 分）

答：

1. `argparse` 这个函数是用于在cli中输入参数
2. `required=True` 代表这个参数是否需要输入
3. `type=positive_float` 负责输入参数的格式规范

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

1. cls() 最终创建的是一个商品的类对象
2. 第二个参数是告诉我们，如果name为空值的话，我们则使用默认值，即空值
3. 因为我们是创建一个商品的类对象，所以要返回Product，但是此时Product类还没创建呢，程序流程还没做完，所以要放在""内避免报错
4. self.name 表示当前商品的name值

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

1. 最终返回一个ProductList结构  llist[dict[str,Any]
2. 异常粒度细分，出异常时可以清楚分辨是哪里有问题
3. 有几个%r就要提供几个参数
4. 不知道

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

1. arrange是准备数据，act是执行我们想要验证的函数，assert是验证当前函数执行是否和预期结果保持一致
2. 被识别为一个测试，因为写在一个  def test_....代码中
3. 不会，必须要这个测试函数中所有的assert都通过才算passed

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

1. name的值是4090，类型是str
2. category的值是空值，当没有category时默认空值
3. max_price的值是10000，类型是flot
4. 属性名不能用-，只能用_，而命令行参数是可以设定-

## 四、命令与协作流程题（共 20 分，每题 5 分）

### 20. 写出以下三条检查命令：编译检查三个模块、Ruff 检查包、运行全部 Pytest。（5 分）

答：

```
python -m ruff check product_app.models product_app.service prodcut_app.cli 
python -m ruff check product_app
python -m pytest -q
```

### 21. 从 `dev_yzy` 创建并切换到 `feature/search-help`，提交修改并首次推送远程分支。写出主要命令顺序。（5 分）

答：

```
git switch feature/search-help
git add .
git commit -m "xxxx"
git push 
```

### 22. PR 已在 GitHub 合并到远程 `dev_yzy`，本地仍停留在旧版本。写出切回 `dev_yzy` 并以 fast-forward 方式同步的命令。（5 分）

答：

```
git pull --ff-on -u origin dev_yzy
```

### 23. 回答以下 Git 问题。（5 分）

1. 用什么命令查看当前分支与 `origin/dev_yzy` 的提交差异？（2 分）
2. 用什么命令安全撤销提交 `5c2d37a` 并保留历史？（2 分）
3. `git tag -a v0.1.0 -m "Product Manager CLI v0.1.0"` 标记的是哪个状态？（1 分）

答：

1. git diff
2. git head~1
3. 标记的是当前的git状态

## 阅卷区

选择题：18 / 20
概念题：18 / 20
代码题：32 / 40
操作题：7 / 20
总分：75 / 100
