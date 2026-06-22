"""
JSON 数据的读取和保存
"""

import json 
import logging
from pathlib import Path
from product_app.models import Product,ProductList

logger = logging.getLogger(__name__)

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
    