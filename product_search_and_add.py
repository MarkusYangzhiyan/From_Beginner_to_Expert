"""
单脚本练习
商品读取、添加和查询：读取products.json,接收用户输入，添加商品或筛选商品，保存修改，显示结果

检索商品
: 1.func load_products()  读取products.json\\
: 2.func get_max_price()      get_filter_conditions的辅助函数，接收并校验用户输入的最高价格 \\
: 3.func get_filter_conditions()  接收用户输入的查询条件  \\
: 4.func filter_products()    根据名称、分类、最高价格筛选商品\\
: 5.func show_products()      把筛选结果打印出来 \\

添加商品：
: 1.func get_new_product()   获得新商品的列表信息
: 2.func add_products()   添加一个新商品到商品列表    \\
: 3.func save_products()  把修改后的商品列表保存回products.json中 \\

主程序
: 1.func main()                    主流程  \\
"""

# =====================================
# 导入必要的包
# =====================================
import json 
import orjson 
import os
from pathlib import Path
from typing import Dict,List,Any



# =====================================
# 1. 基础环境配置
# =====================================
PRODUCT_PATH = Path(__file__).resolve().parent / 'data' / 'processed' / 'products.json'


# =====================================
# 2. load_products()  从prodcuts.json中加载数据
# =====================================

def load_products(file_path:Path) -> Dict[str,Any]:
    try:
        text = file_path.read_text(encoding = 'utf-8')
        return json.loads(text)
        
    except FileNotFoundError:
        print(f" Can not Found {file_path}")
        return []
    
    except json.JSONDecodeError as e:
        print(f"there is an error when parse {file_path}, error:{e}")
        return []

# =====================================
# 3. save_products()  把修改后的商品列表保存回products.json
# =====================================

def save_products(file_path:Path,products:Dict[str,Any]):
    file_path.parent.mkdir(parents= True,exist_ok = True)

    json_text = json.dumps(
        products,
        ensure_ascii=False,
        indent=2
    )

    file_path.write_text(json_text,encoding = 'utf-8')

# =====================================
# 4. filter_prodcuts()  根据信息筛选商品
# =====================================

def filter_products(
        products:Dict[str,Any],
        name:str,
        category:str,
        max_price:int,
) -> Dict[str,Any]:
    
    results = []

    for product in products:
        product_name = product.get("name","")
        product_price = product.get("price")
        product_categories = product.get("category",[])

        if isinstance(product_categories,str):
            product_categories = [product_categories]

        if name and name.lower() not in product_name.lower():
            continue 

        if category:
            match_category = False

            for product_category in product_categories:
                if category.lower() in product_category.lower():
                    match_category = True
                    break 
            if not match_category:
                continue 

        if max_price is not None:
            if not isinstance(product_price,(int,float)):
                continue 

            if product_price > max_price:
                continue 
        
        results.append(product)

    return results

# =====================================
# 5. show_prodcuts()  显示商品
# =====================================

def show_products(results:Dict[str,Any]) -> Dict[str,Any]:
    if not results:
        print("there is no matched product can be shown")
        return 

    print("\n 筛选结果:")

    for product in results:
        print(
            f"product_name:{product.get("name")}\n"
            f"product_category:{product.get("category")}\n"
            f"product_price:{product.get("price")}\n"
        )

# =====================================
# 6. get_max_price()  处理价格输入
# =====================================

def get_max_price():
    while True:
        price_text = input("最高价格，直接回车表示不限：").strip()

        if not price_text:
            return None
        
        try:
            max_price = float(price_text)
        except ValueError:
            print("价格必须是数字，请重新输入")
            continue 

        if max_price <= 0:
            print("价格必须大于0，请重新输入")
            continue 

        return max_price 
    
# =====================================
# 7. get_filter_conditions()   接收用户输入的查询条件
# =====================================

def get_filter_conditions():
    name = input("产品名称，直接回车表示不限：").strip()
    category = input("产品分类，直接回车表示不限：").strip()
    max_price = get_max_price()

    return name,category,max_price

# =====================================
# 8. get_new_product()   获得新商品的列表信息
# =====================================

def get_new_product():
    name = input("新产品名称：").strip()

    if not name:
        print("产品名称不能为空")
        return None
    
    category = input("新产品类型：").strip()

    if not category:
        print("产品分类不能为空")
        return None
    
    while True:
        price_text = input("新产品价格：").strip()

        try:
            price = float(price_text)
        except ValueError:
            print("价格必须是数字，请重新输入")
            continue 

        if price <= 0:
            print("价格必须大于0，请重新输入")
            continue 

        break 
    
    return {
        "id": None,
        "name": name,
        "price": price,
        "category": [category],
        "rating": None,
        "rating_count": 0,
        "store": "自定义商品",
    }


# =====================================
# 9. add_product()   添加商品到prodcuts.json中
# =====================================

def add_product(products,file_path):
    new_product  = get_new_product()

    if new_product is None:
        print("添加商品失败")
        return products
    
    products.append(new_product)

    save_products(file_path,products)

    print("商品已添加并保存")

    return products

# =====================================
# 10. main()  主程序流程  
# =====================================

def main():
    products = load_products(PRODUCT_PATH)

    if not products:
        print("没有可用的商品数据，程序结束")
        return 
    
    while True:
        print("\n== 商品管理器 ==")
        print("1. 查询商品")
        print("2. 添加商品")
        print("q. 退出程序")

        choice = input("请选择操作：").strip()

        if choice.lower() == 'q':
            print("程序已退出")
            break 

        if choice == "1":
            name,category,max_price = get_filter_conditions()

            results = filter_products(
                products = products,
                name = name,
                category = category,
                max_price = max_price
            )

            show_products(results)

        elif choice == "2":
            products = add_product(products,PRODUCT_PATH)

        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main()