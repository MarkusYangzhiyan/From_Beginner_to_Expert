"""
放业务逻辑，比如读取、保存、筛选、添加商品
"""

# =====================================
# 导入必要的包
# =====================================
import json 
from pathlib import Path
from product_app.models import Product, ProductList
import logging 

logger = logging.getLogger(__name__)

# =====================================
# 基础环境配置
# =====================================
PRODUCT_PATH = Path(__file__).resolve().parent.parent / 'data' / 'processed' / 'products.json'


# =====================================
# load_products()  从prodcuts.json中加载数据
# =====================================

def load_products(file_path: Path) -> ProductList:
    try:
        text = file_path.read_text(encoding = 'utf-8')
        product_dicts = json.loads(text)
        return [Product.from_dict(item) for item in product_dicts]
        
    except FileNotFoundError:
        logger.error("Can not Found %r",file_path)
        return []
    
    except json.JSONDecodeError as e:
        logger.error("there is an error when parse %r, error: %r",file_path,e)
        return []
    

# =====================================
# save_products()  把修改后的商品列表保存回products.json
# =====================================

def save_products(file_path: Path,products: ProductList) -> None:
    file_path.parent.mkdir(parents= True,exist_ok = True)
    
    # 此时的products的格式为 [Product(...),Product(...),...]
    product_dicts = [product.to_dict() for product in products]
    json_text = json.dumps(
        product_dicts,
        ensure_ascii=False,
        indent=2
    )
    file_path.write_text(json_text,encoding = 'utf-8')

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
        new_product: Product,
        file_path: Path
) -> ProductList:
    
    products.append(new_product)

    save_products(file_path,products)

    logger.info("商品 % r 已添加并保存",new_product.name)

    return products
