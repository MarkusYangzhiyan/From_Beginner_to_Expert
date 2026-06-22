"""
组合模块并启动程序
"""

import logging
from product_app.cli import (
    MenuChoice,
    get_filter_conditions,
    get_new_product,
    show_products
)
from product_app.repository import (
    PRODUCT_PATH,
    load_products,
    save_products
)
from product_app.service import (
    add_product,filter_products
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
            
            products = add_product(products,new_product)
            save_products(PRODUCT_PATH,products)

        else:
            print("无效选择，请重新输入")


if __name__ == "__main__":
    main()