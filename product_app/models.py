"""
存放数据结构，比如说product类型
"""

from dataclasses import dataclass
from typing import Any 

@dataclass
class Product:
    id:str | None
    name:str
    category:list[str]
    price:float 
    rating:float | None = None
    rating_count:int = 0 
    store:str | None = None

    @classmethod
    def from_dict(cls,data:dict[str,Any]) -> "Product":     # cls 代表类本身
        """把一个商品字典转换成 Product 对象。"""
        
        category = data.get("category",[])

        if isinstance(category,str):
            category = [category]

        return cls(
            id = data.get("id"),
            name = data.get("name",""),
            category = category,
            price = float(data.get("price",0)),
            rating = data.get("rating"),
            rating_count = data.get("rating_count") or 0 ,
            store = data.get("store")
        )
    
    # 对象方法
    def to_dict(self) -> dict[str,Any]:
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "category":self.category,
            "rating":self.rating,
            "rating_count":self.rating_count,
            "store":self.store
        }
    
ProductList = list[Product]
