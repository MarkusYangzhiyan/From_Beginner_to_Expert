products = [
    {"name": "笔记本电脑", "category": "电脑", "price": 5999},
    {"name": "机械键盘", "category": "外设", "price": 399},
    {"name": "无线鼠标", "category": "外设", "price": 129},
    {"name": "显示器", "category": "办公", "price": 1599},
    {"name": "USB-C扩展坞", "category": "外设", "price": 299},
]


def filter_product(name = "", category = "", max_price = None):

    results = []
    for product in products:
        if name and name not in product["name"]:
            continue 

        if category and category != product['category']:
            continue 
        
        if max_price is not None and product['price'] > max_price:
            continue

        results.append(product)

    return results


def show_products(results):

    if not results:
        print("没有找到符合条件的产品")
        return 
    
    print("\n 筛选结果")