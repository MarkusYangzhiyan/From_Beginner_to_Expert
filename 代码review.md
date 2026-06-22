# source: From_Beginner_to_Expert\prepare_products.py
## --------------------------------------------------------------

## 2026-06-19

### 1. 

```
def test_sort_product_by_price_ascending():
```

这个函数是用于pytest测试的，放在tests/test_service.py下
但是函数名必须开头是test_.... 
否则在终端输入  python -m pytest tests/test_service.py 将捕捉不到这个测试函数

### 2.

```
# AAA测试

def test_.....():

    # arrange：准备测试数据

    # act：执行被测试数据

    # assert：验证结果是否符合预期
```


### 3. 

```
def test_....(tmp_file):

```

这里的tmp_file是 pytest 提供的临时目录，用完会自动清理。
可以用来测试加载数据的格式是否错误






## --------------------------------------------------------------
## 2026-06-18

### 1. 

```
@classmethod
def from_dict(cls,data:dict[str,Any]) -> "Product":


def to_dict(self):
```
1. 使用@classmethod代表类方法，不需要再用 def func(self,data) 这种方式，不需要写self了
2. cls代表类本身
3. "Product" 加""是因为此时Product类还在创建中
4. from_dict是类方法，to_dict是对象方法。调用时不同： Product.from_dict(data) vs product.to_dict()

### 2.

```
python -m ruff check product_app

python -m ruff check product_app --fix
```

1. ruff 是一个python包，是用来检查代码质量和代码风格的工具
2. 可以用python -m ruff check [代码] --fix 来自动修复


### 3. 

```
logger = logging.gerLogger(__name__) 

def setup_logging(
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers = [
            logging.StreamHandler(),
            logging.FileHandler("app.log",encoding = 'utf-8')
        ]
    )
)
```

上一个代码是用于终端打印的
下一个代码是在文件日志中保存记录


## --------------------------------------------------------------
## 2026-06-15

### 1.

```
for line_number,line in enumerate(line,start = 1)
```

在遍历内容的同时生成序号,序号从1开始

### 2.

```
json.loads()  
```

把 json 格式的字符串转换成 python 字典数据

```
json.dumps()
```

把 python 字典数据转换成 json 格式的字符串

### 3.

```
except (gzip.BadGzipFile or OSError) as error:
```

BadGzipFile: 文件不是有效的 gzip 压缩文件，或者压缩文件已经损坏
OSError: 表示操作系统层面的输入输出错误
这一行error都表示文件无法读取或者解析，而 except FileNotFound 是找不到文件，两种不同的错误

### 4.

```
for line_number,line in enumerate(file_path,start = 1):
    .....
    if len(products) >= num_products:
        break 
```

这里 break 指的是结束当前这个 for 循环， for 循环后面的代码继续执行
和 continue 的区别： continue 是跳过当前循环的这一轮，继续执行 for 循环的下一轮，而 break 直接结束 for 循环

### 5.

```
json.dumps(
    products,
    ensure_ascii=False,
    indent=2,
)
```

json.dumps: 从 pyton 的字典数据 转换成 json格式
ensure_ascii  = False : 保留 中文原文，不要转换成 ascii 格式
indent = 2： json格式保留 2 格缩进，规范格式，便于阅读

### 6.

```
import json 
import orjson 

json.dumps()
orjson.dumps()
```

json.dumps：纯python 速度慢 |   返回str
orjson.dumps：Rust写的，速度快3-5倍 |   返回 bytes
