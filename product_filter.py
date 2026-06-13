products = [
    {"name": "笔记本电脑", "category": "电脑", "price": 5999},
    {"name": "机械键盘", "category": "外设", "price": 399},
    {"name": "无线鼠标", "category": "外设", "price": 129},
    {"name": "显示器", "category": "办公", "price": 1599},
    {"name": "USB-C扩展坞", "category": "外设", "price": 299},
]


def filter_product(name="",category="",max_price=None):

    """
    根据名称、分类和最高价格筛选出产品
    """

    results = []

    for product in products:

        if name and name not in product["name"]:
            continue 

        if category and category != product["category"]:
            continue 

        if max_price is not None and max_price < product["price"]:
            continue 

        results.append(product)

    return results


def show_products(results):

    if not results:
        print("没有找到符合条件的产品")
        return 
    
    print("\n 筛选结果")

    for product in results:
        print(
            f"产品名称：{product["name"]}",
            f"产品分类：{product["category"]}",
            f"最高价格：{product['price']}"
        )



while True:

    print("\n == 产品筛选器 == ")
    print("直接回车表示不限制条件，输入 q 退出程序")

    name = input("产品名称：").strip()

    if name.lower() == "q":
        print("程序已退出")
        break 

    category = input("产品类型：").strip()
    price_text = input("最高价格：").strip()

    if price_text:
        try:
            max_price = float(price_text)
        except ValueError:
            print("价格必须是数字，请重新输入。")
            continue 
    else:
        max_price = None


    matched_products = filter_product(
        name = name,
        category=category,
        max_price=max_price
    )
    show_products(matched_products)