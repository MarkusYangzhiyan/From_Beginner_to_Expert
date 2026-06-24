# 第一周测试卷：Python 基础、文件处理与基础 Git

## 批阅结果

**最终得分：72 / 100****答题用时：约 42 分 52 秒****成绩评价：合格，基础概念较稳，关键细节和命令准确性需要加强。**

> 用时根据文件创建时间 `15:41:40` 与最后提交修改时间 `16:24:32`
> 估算，只代表文件记录的答题时间窗口。

### 分项成绩

| 部分             |         得分 |          满分 |
| ---------------- | -----------: | ------------: |
| 基础选择题       |           20 |            20 |
| 概念简答题       |           17 |            20 |
| 代码阅读题       |           26 |            40 |
| 命令与故障处理题 |            9 |            20 |
| **总分**   | **72** | **100** |

### 逐题得分

| 题号 | 得分 | 满分 | 批阅说明                                                                                                        |
| ---- | ---: | ---: | --------------------------------------------------------------------------------------------------------------- |
| 1-10 |   20 |   20 | 选择题全部正确。                                                                                                |
| 11   |    3 |    4 | 商品示例正确；还应指出列表是有顺序的元素集合，字典是键值映射。                                                  |
| 12   |    3 |    4 | 参数和返回值理解正确；还应提到函数便于复用、测试和职责拆分。                                                    |
| 13   |    4 |    4 | 对相对项目位置和可移植性的解释准确。                                                                            |
| 14   |    3 |    4 | 知道不能只看 `except` 数量；定义还应强调异常分类和处理的具体程度。                                            |
| 15   |    4 |    4 | 正确指出可逐步执行、观察中间状态，并减少临时 `print()`。                                                      |
| 16   |    6 |   10 | 直接回车应返回 `None`；`abc` 在 `float(price_text)` 处触发 `ValueError`；负数被拒绝，但代码允许 `0`。 |
| 17   |    6 |   10 | 子字符串和大小写理解正确；`max_price is not None` 表示最高价是可选条件，并非必须输入。                        |
| 18   |    8 |   10 | `"rt"` 是文本读取模式，不是二进制模式；其余理解正确。                                                         |
| 19   |    6 |   10 | `ensure_ascii=False` 控制非 ASCII 字符是否转义，与二进制无关；最后一行把 JSON 文本写入文件并覆盖原内容。      |
| 20   |    2 |    5 | 模块和解释器顺序写错；PowerShell 激活路径建议带 `.\` 形式的相对路径前缀。                                     |
| 21   |    5 |    5 | `add`、`commit`、`push` 可以正确把本地删除同步到远程。                                                    |
| 22   |    2 |    5 | 它表示没有新的本地提交可推送；暂存区内容不能被 `push`，必须先 `commit`。                                    |
| 23   |    0 |    5 | 正确异常是 `FileNotFoundError` 和 `json.JSONDecodeError`，题目要求返回 `[]`。                             |

### 重点订正

1. 直接回车后 `price_text == ""`，因此 `if not price_text` 成立并返回 `None`。
2. `max_price is not None` 的含义是“用户提供了最高价格时才进行价格筛选”。
3. gzip 的 `"rt"` 是 read text，`"rb"` 才是 read binary。
4. `ensure_ascii=False` 让中文等 Unicode 字符直接显示，而不是写成 `\uXXXX`。
5. 创建和激活 Python 3.12 虚拟环境可使用：

   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
6. `git push` 只推送提交记录，不会推送仅经过 `git add` 的暂存内容。
7. 文件不存在和 JSON 解析失败分别对应：

   ```python
   except FileNotFoundError:
       return []
   except json.JSONDecodeError:
       return []
   ```

   返回空列表可以保持函数返回类型稳定，让调用方继续按照“商品列表”处理；但它也可能掩盖错误，所以必须同时记录日志。

考试范围：Day 001-Day 007
建议时间：75 分钟
满分：100 分
姓名：__Markus________  日期：___2026-06-24_______  得分：__72 / 100__

## 答题说明

1. 本卷不要求编写完整项目，只需回答概念、命令、运行结果和关键代码。
2. 命令题允许写功能等价的命令。
3. 请直接在每道题的“答：”后填写答案，不要修改题目。

## 一、基础选择题（共 20 分，每题 2 分）

### 1. 下列哪个 Python 类型最适合保存一条具有 `name`、`price`、`category` 字段的商品？（2 分）

A. `str`
B. `dict`
C. `bool`
D. `float`

答：b

### 2. `input("名称：").strip()` 中的 `strip()` 主要作用是什么？（2 分）

A. 把字符串转换成数字
B. 删除字符串两端的空白字符
C. 删除字符串中所有空格
D. 判断字符串是否为空

答：b

### 3. `enumerate(file, start=1)` 中的 `start=1` 表示什么？（2 分）

A. 从文件第二行开始读取
B. 行号从 1 开始计数
C. 每次读取一个字符
D. 最多读取一行

答：b

### 4. `json.loads(text)` 的作用是什么？（2 分）

A. 把 Python 对象转换为 JSON 文本
B. 把 JSON 文本解析为 Python 对象
C. 把文件压缩为 gzip
D. 把字符串转换为浮点数

答：b

### 5. 如果 `categories = ["Beauty", "Makeup", "Lipstick"]`，`categories[-1]` 的结果是什么？（2 分）

A. `"Beauty"`
B. `"Makeup"`
C. `"Lipstick"`
D. 报错

答：c

### 6. 循环中的 `continue` 表示什么？（2 分）

A. 结束整个函数
B. 跳过本轮循环，继续下一轮
C. 结束所有循环
D. 返回一个空列表

答：b

### 7. 循环中的 `break` 表示什么？（2 分）

A. 退出当前所在的最近一层循环
B. 一定结束整个函数
C. 忽略当前异常
D. 删除当前数据

答：a

### 8. `directory.mkdir(parents=True, exist_ok=True)` 的含义是什么？（2 分）

A. 只在目录已经存在时创建
B. 创建目录；缺失的父目录也一起创建；已存在时不报错
C. 创建一个普通文件
D. 删除并重新创建目录

答：b

### 9. `except json.JSONDecodeError` 主要捕获哪类问题？（2 分）

A. 文件路径不存在
B. JSON 文本格式无法正确解析
C. Git 推送失败
D. 用户输入了负数

答：b

### 10. 将本地修改发送到远程 Git 仓库，常见的正确顺序是什么？（2 分）

A. `push -> add -> commit`
B. `commit -> push -> add`
C. `add -> commit -> push`
D. `add -> push -> commit`

答：c

## 二、概念简答题（共 20 分，每题 4 分）

### 11. 简述列表 `list` 和字典 `dict` 的区别，并分别举一个商品程序中的用途。（4 分）

答：

1. 首先外观不同  list:[] , dict :{}
2. 我理解的是，list中存的是多个对象，而dict中存的是一个对象的多个属性
3. 在目前我们的product manager cli 中， dict是存一个商品的id，name，category等属性，list是存多个商品

### 12. 函数的“参数”和“返回值”分别是什么？为什么筛选逻辑适合写成函数？（4 分）

答：

1. 参数是写在def 括号内的东西，我可以理解成函数运行需要输入的东西，而返回值是函数运行结束后输出的东西
2. 因为筛选逻辑中，对于一个商品的筛选，会有多个参数多个要求，而返回值是一个大的list，包括筛选出来的多个商品，写成一个函数更加方便可观。

### 13. `Path(__file__).resolve().parent` 大致表示什么？相比直接写固定绝对路径有什么好处？（4 分）

答：

1. 先定位到该文件，然后获得该文件的绝对路径，然后获得该文件的父目录的绝对路径
2. 比固定绝对路径的好处是可复用，即使别人clone了我的代码到别的磁盘或者别的根目录中，也可以运行，但是固定绝对路径的话，到别人的环境下或者电脑中不同的位置，运行就会报错了

### 14. 什么是“异常处理粒度”？是否可以简单认为 `except` 数量越多，粒度就一定越细？说明理由。（4 分）

答：

1. 异常处理粒度就是使用try-except方法，我们自己先列出可能出现的异常情况，提前设置好异常提示
2. 一般情况下，except越多，粒度越细，但是有的时候，好几个except可能属于一个粒度，如果分开写的话，看起来会很乱，这种情况下需要判断是否属于同一个粒度并且合并

### 15. VS Code 断点调试与在代码中大量添加 `print()` 相比，有什么优势？至少写两点。（4 分）

答：

1. 断点调试可以控制每个断点处运行，也就是说，假设有多个断点，我可以认为控制一个断点一个断点输出看情况，如果第一个断点没问题了，我可以人为按F5进行下一个断点
2. 大量的print代码比较乱，在终端输出的内容太多了

## 三、代码阅读与关键代码题（共 40 分，每题 10 分）

### 16. 阅读最高价格输入代码。（10 分）

```python
def get_max_price() -> float | None:
    price_text = input("最高价格：").strip()

    if not price_text:
        return None

    try:
        max_price = float(price_text)
    except ValueError:
        return None

    if max_price < 0:
        return None

    return max_price
```

回答：

1. 直接回车时返回什么？（2 分）
2. 输入 `abc` 时，哪一行会触发异常，最终返回什么？（3 分）
3. 输入 `-10` 时返回什么？为什么？（2 分）
4. 输入 `99.5` 时返回值及其类型是什么？（3 分）

答：

1. 直接回车终端会返回一个输入框，让用户输入最高价格
2. 输入abc时会 第9行会触发异常，最终返回空值
3. 输入-10会返回空值，因为第12行要求输入需要大于0
4. 输入99.5时返回值是99.5，类型是float

### 17. 阅读商品筛选代码。（10 分）

```python
for product in products:
    if name and name.lower() not in product["name"].lower():
        continue

    if category and category.lower() not in product["category"].lower():
        continue

    if max_price is not None and product["price"] > max_price:
        continue

    results.append(product)
```

回答：

1. 为什么名称判断使用 `not in`，而不是 `!=`？（3 分）
2. 为什么要调用 `lower()`？（2 分）
3. `max_price is not None` 的目的是什么？（2 分）
4. 商品什么时候会被加入 `results`？（3 分）

答：

1. 如果用！=，则要求name完全相同，但实际上，名称输入类似，用户知道是同一个东西，但不会完全相同，比如说自行车和山地自行车，都属于自行车
2. 调用lower（）是把用户输入和条件都变小写，避免用户输入Q，程序无法识别
3. 这是筛选要求，用户必须输入最高价格作为商品的一个筛选条件
4. 当名称相同或属于名称的一部分，并且类型相同或者属于类型列表中的一个，并且有最大价格输入且输入符合规范时，商品会被加入results

### 18. 阅读 gzip 和 JSON Lines 处理代码。（10 分）

```python
with gzip.open(file_path, "rt", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        item = json.loads(line)
        name = item.get("title", "").strip()

        if not name:
            continue

        products.append({"name": name})

        if len(products) >= num_products:
            break
```

回答：

1. `"rt"` 表示以什么方式读取 gzip 文件？（2 分）
2. 名称为空时会发生什么？（2 分）
3. `break` 后是立即结束整个函数，还是先退出循环？（3 分）
4. 为什么这里对每一行分别使用 `json.loads(line)`？（3 分）

答：

1. rt是以二进制的方式读取
2. 名字为空时，本轮循环跳过，进入下一轮循环
3. 先退出当前循环，然后继续下面的代码
4. 因为每一行读取的都是json，我们需要转成python的list或者dict形式

### 19. 阅读 JSON 保存代码。（10 分）

```python
def save_products(file_path: Path, products: list[dict]) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    json_text = json.dumps(products, ensure_ascii=False, indent=2)
    file_path.write_text(json_text, encoding="utf-8")
```

回答：

1. `file_path.parent` 是什么？（2 分）
2. `ensure_ascii=False` 有什么作用？（3 分）
3. `indent=2` 有什么作用？（2 分）
4. 最后一行完成了什么操作？（3 分）

答：

1. file_path的父目录
2. 不使用二进制写入，这样我们可以看到字母和文字
3. json换行时缩进2格，格式规范好看
4. 把python的list或者dict的内容，写进到空的file_path中

## 四、命令与故障处理题（共 20 分，每题 5 分）

### 20. 在项目根目录创建 Python 3.12 虚拟环境、激活环境，各写一条 PowerShell 命令。（5 分）

答：

```
# 创建虚拟环境
python -m py3.12 venv .venv 

# 激活环境
.venv\Scripts\activate.ps1

```

### 21. 本地已经删除了被 Git 跟踪的 `prepare_products.py`。写出让远程仓库也删除它所需的三个主要 Git 命令。（5 分）

答：

```
git status 
git add prepare_products.py
git commit -m "delete file"
git push 

```

### 22. 执行 `git push` 后显示 `Everything up-to-date`，它表示什么？为什么只有 `git add`、没有 `git commit` 时会出现这种情况？（5 分）

答：

1. 表示所有在本地加到git分支的代码都已经同步提交到git远程代码仓库了
2. 这个问题我不知道

### 23. `load_products()` 需要分别处理“文件不存在”和“JSON 格式错误”。写出两个对应的异常类型，并说明发生错误后返回空列表的意义。（5 分）

答：

```python-repl
try:
	pass 
except FileNotFound:
	return None
except json.JSONEncoderError:
	return None

```

我不知道为什么要返回空列表

## 阅卷区

选择题：20 / 20
概念题：17 / 20
代码题：26 / 40
操作题：9 / 20
总分：72 / 100
