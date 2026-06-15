import json 
from pathlib import Path

DATA_FILE = (
    Path(__file__).resolve().parent / 'data' / 'processed' / 'products.json'
)

def load_products(file_path):
    try:
        text = file_path.read_text(encoding = 'utf-8')
        return json.loads(text)
    
    except FileNotFoundError:
        print(f'{file_path} is not found')
        return []
    
    except json.JSONDecodeError as error:
        print(
            f'json schema is wrong:'
            f'{error.lineno} row,'
            f'{error.colno} col'
        )
        return []
    
products = load_products(DATA_FILE)


def filter_product(name="",category="",max_price=None):

    """
    根据名称、分类和最高价格筛选出产品
    """

    results = []

    for product in products:

        if name and name not in product["name"]:
            continue 

        if category and category not in product["category"]:
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