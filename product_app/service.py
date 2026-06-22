"""
查询、排序、添加等业务逻辑
"""

# =====================================
# 导入必要的包
# =====================================
from product_app.models import Product, ProductList
import logging 

logger = logging.getLogger(__name__)


# =====================================
# filter_prodcuts()  根据信息筛选商品
# =====================================

def filter_products(
        products: ProductList,
        name: str = "",
        category: str = "",
        max_price: float | None = None,
) -> ProductList:
    
    results = []

    for product in products:
        product_name = product.name
        product_price = product.price
        product_categories = product.category

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
# add_product()   添加商品到prodcuts.json中
# =====================================

def add_product(
        products: ProductList,
        new_product: Product
) -> ProductList:
    
    products.append(new_product)

    logger.info("商品 %r 已添加",new_product.name)

    return products


def sort_products_by_price(
        products: ProductList,
        reverse : bool = False
) -> ProductList:
    
    return sorted(
        products,
        key = lambda product : product.price,
        reverse = reverse
    )

