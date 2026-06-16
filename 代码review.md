# 2026-06-15

## source: From_Beginner_to_Expert\prepare_products.py

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
