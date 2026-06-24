from fastapi import FastAPI
from typing import Any
from product_app.repository import load_products,PRODUCT_PATH

app = FastAPI(
    title = 'product manager cli',
    version = '0.1.0'
)


# 当客户端用get方法访问 /health 时，执行下面的函数。
@app.get("/health")
def health() -> dict[str,str]:
    return {'status':'ok'}

@app.get("/products")
def get_products() -> list[dict[str,Any]]:
    products = load_products(PRODUCT_PATH)
    
    return  [product.to_dict() for product in products]