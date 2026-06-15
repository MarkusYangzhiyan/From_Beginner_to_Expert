import gzip 
import json 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SOURCE_FILE = BASE_DIR / "data" / "raw" / "meta_All_Beauty.jsonl.gz"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "products.json"

num_products = 1000

def load_and_clean_products(file_path,num_products):

    products = []

    try:
        with gzip.open(file_path,"rt",encoding = "utf-8") as file:
            
            for line_number, line in enumerate(file,start  = 1):
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:    
                    print(f"第{line_number}行json格式错误")
                    continue

                name = item.get("title","").strip()
                price = item.get("price")   

                if not name :
                    continue 

                if not isinstance(price,(int,float)) or price <= 0:
                    continue 

                categories = item.get("categories") or []

                if categories:
                    category = categories
                else:
                    category = item.get("main_category") or "未分类"

                product = {
                    "id":item.get("parent_asin"),
                    "name": name,
                    "price":price,
                    "category":category,
                    "rating":item.get("average_rating"),
                    "rating_count":item.get("rating_number"),
                    "store":item.get('store')
                }

                products.append(product)

                if len(products) >= num_products:
                    break   
    except FileNotFoundError:
        print(f'{file_path} is not found !')
        return []
    
    except (gzip.BadGzipFile,OSError) as error:
        print(f'there is an error when reading file : {error}')
        return []
    
    return products



def save_products(file_path,products):
    file_path.parent.mkdir(parents = True,exist_ok = True)

    json_text = json.dumps(
        products,
        ensure_ascii=False,
        indent = 2
    )


    file_path.write_text(json_text,encoding = 'utf-8')


products = load_and_clean_products(SOURCE_FILE,num_products)

if products:
    save_products(OUTPUT_FILE,products)
    print(f'there are {len(products)} products have been saved')
    print(f'output_file path is {OUTPUT_FILE}')


DATA_FILE = (
    Path(__file__).resolve().parent / 'data' / 'processed' / 'products.json'
) 

new_product = {
    "id":"yzy123",
    "name": "测试产品",
    "price":100,
    "category":"测试类别",
    "rating":1.0,
    "rating_count":1,
    "store":""
}
products.append(new_product)
save_products(DATA_FILE,products)
