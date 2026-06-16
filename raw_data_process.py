"""
原始数据处理：负责一次性导入和准备数据

: func load_and_clean_products():读取gzip压缩数据，逐行解析JSONL，清洗脏数据
: save_products(): 把清洗好的数据保存成 .json
: main(): 主流程
"""

# =====================================
# 导入必要的包
# =====================================

import gzip 
import json 
import orjson
from pathlib import Path
from typing import List,Dict,Any

# =====================================
# 1. 基础环境配置
# =====================================
SOURCE_FILE = Path(__file__).resolve().parent / 'data' / 'raw' / 'meta_All_Beauty.jsonl.gz'
OUTPUT_FILE = Path(__file__).resolve().parent / 'data' / 'processed' / 'products.json'
MAX_NUMBER_PRODUCTS = 1000

# =====================================
# 2. load_and_clean_products 读取压缩数据，逐行解析并清洗脏数据
# =====================================
 
def load_and_clean_products(
        input_file_path:str,
        max_number_products: int = 1000
) -> Dict[str,Any]:
    
    products = []

    try:
        with gzip.open(input_file_path,"rt",encoding = 'utf-8') as file:
            for linenumber, line in enumerate(file,start = 1):
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    print(f"there is an error when parse the {linenumber} line, pass it and continue the next line")
                    continue 
                name = item.get("title","").strip()
                price = item.get("price")
                categories = item.get("categories") or []

                if not name:
                    continue 

                if not price or not isinstance(price,(int,float)) or price <= 0:
                    continue 
                
                if not categories or not isinstance(categories,list):
                    main_category = item.get("main_category") or "未分类"
                    categories = [main_category]

                product = {
                    "id":item.get("parent_asin"),
                    "name": name,
                    "price": price,
                    "category": categories,
                    "rating": item.get("average_rating"),
                    "rating_count": item.get("rating_number"),
                    "store": item.get("store"),
                }

                products.append(product)

                if len(products) >= max_number_products:
                    break 

    except FileNotFoundError:
        print(f" Can not found {input_file_path}")
        return []
    
    except (gzip.BadGzipFile,OSError) as e:
        print(f"Fail to parse {input_file_path}, error:{e}")
        return []
    
    return products


# =====================================
# 2. save_products()  把清洗好的数据保存成json文件
# =====================================

def save_products(
        output_file_path:str,   
        products:Dict[str,Any]
) -> None:
    output_file_path.parent.mkdir(parents = True,exist_ok = True)

    json_text = json.dumps(
        products,
        ensure_ascii= False,
        indent = 2
    )

    output_file_path.write_text(json_text,encoding = 'utf-8')


# =====================================
# 2. main()  主流程
# =====================================

def main():
    products = load_and_clean_products(SOURCE_FILE,MAX_NUMBER_PRODUCTS)

    if not products:
        print(f'It is empty in products')
        return 
    
    save_products(OUTPUT_FILE,products)

    print(f"Save Success, there are {len(products)} products")
    print(f"output file path is {OUTPUT_FILE}")
    print(f"Here is an example")

    for product in products[:3]:
        print(product)



if __name__ == "__main__":
    main()