# 产品信息展示与数据校验练习

"""
学习笔记：
1. strip() : 用于处理string, 去除string对象前后的空白空格,但不会删除中间的空格
"""

products = [
    {"name":"笔记本电脑","price":5999},
    {"name":"机械键盘","price":399},
    {"name":"无线鼠标","price":129},
    {"name":"","price":129},
    {"name":"显示器","price":-100},
]

for product in products:
    name = product["name"]
    price = product["price"]

    if not name.strip():
        print("错误：产品名不能为空")
    elif price <= 0:
        print(f"错误：{name}的价格不合法")
    else:
        print(f"产品：{name}，价格：{price}")

    