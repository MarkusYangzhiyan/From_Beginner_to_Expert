"""
input、print、菜单和输入校验
"""

from enum import Enum
from product_app.models import Product,ProductList
import logging 

logger = logging.getLogger(__name__)

class MenuChoice(str,Enum):
    SEARCH = "1",
    ADD = "2",
    QUIT = "q"


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

