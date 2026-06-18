"""
放用户交互和主流程
"""

from product_app.models import Product,ProductList
from enum import Enum
import logging 
from product_app.service import (
    PRODUCT_PATH,
    add_product,
    filter_products,
    load_products
)

def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("app.log",encoding = 'utf-8')
        ]
    )

logger = logging.getLogger(__name__)

class MenuChoice(str,Enum):
    SEARCH = "1",
    ADD = "2",
    QUIT = "q"

# =====================================
# show_prodcuts()  显示商品
# =====================================

def show_products(
        results: ProductList,
        name: str = "",
        category: str = "",
        max_price: float | None = None
) -> None:
    if not results:
        logger.info("No matched products found.query_name =%r,query_category=%r,query_price=%r",
                    name,  
                    category,
                    max_price)
        print("there is no matched product can be shown")
        return 

    print("\n 筛选结果:")

    for product in results:
        print(
            f"product_name:{product.name}\n"
            f"product_category:{product.category}\n"
            f"product_price:{product.price}\n"
        )

# =====================================
# get_max_price()  处理价格输入
# =====================================

def get_max_price() -> float | None:
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
# get_filter_conditions()   接收用户输入的查询条件
# =====================================

def get_filter_conditions() -> tuple[str,str,float | None]:
    name = input("产品名称，直接回车表示不限：").strip()
    category = input("产品分类，直接回车表示不限：").strip()
    max_price = get_max_price()

    return name,category,max_price

# =====================================
# get_new_product()   获得新商品的列表信息
# =====================================

def get_new_product() -> Product | None:
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
    
    return Product(
        id=None,
        name=name,
        price=price,
        category=[category],
        rating=None,
        rating_count=0,
        store="自定义商品",
    )

# =====================================
# main()  主程序流程  
# =====================================

def main() -> None:
    setup_logging()

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

        if choice.lower() == MenuChoice.QUIT.value:
            print("程序已退出")
            break 

        if choice == MenuChoice.SEARCH.value:
            name,category,max_price = get_filter_conditions()

            results = filter_products(
                products = products,
                name = name,
                category = category,
                max_price = max_price
            )

            show_products(results,name,category,max_price)

        elif choice == MenuChoice.ADD.value:
            new_product = get_new_product()
            
            if new_product is None:
                print("添加商品失败")
                continue 
            
            products = add_product(products,new_product,PRODUCT_PATH)

        else:
            print("无效选择，请重新输入")


if __name__ == "__main__":
    main()