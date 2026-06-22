"""
组合模块并启动程序
"""

import logging
import argparse
from product_app.models import Product
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


def positive_float(value: str) -> float:
    try:
        number = float(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("价格必须是数字") from error

    if number <= 0:
        raise argparse.ArgumentTypeError("价格必须大于 0")

    return number 

def non_empty_text(value: str) -> str:
    cleaned_value = value.strip()

    if not cleaned_value:
        raise argparse.ArgumentTypeError("内容不能为空")

    return cleaned_value


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Product Manager CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    search_parser = subparsers.add_parser(
        "search",
        help="查询商品",
    )

    search_parser.add_argument(
        "--name",
        default="",
        help="商品名称",
    )

    search_parser.add_argument(
        "--category",
        default="",
        help="商品分类",
    )

    search_parser.add_argument(
        "--max-price",
        type=positive_float,
        default=None,
        help="最高价格",
    )

    add_parser = subparsers.add_parser(
        "add",
        help="添加商品",
    )

    add_parser.add_argument(
        "--name",
        required=True,
        type=non_empty_text,
        help="商品名称",
    )

    add_parser.add_argument(
        "--category",
        required=True,
        type=non_empty_text,
        help="商品分类",
    )

    add_parser.add_argument(
        "--price",
        required=True,
        type=positive_float,
        help="商品价格",
    )
    return parser


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
    parser = create_parser()
    args = parser.parse_args()

    setup_logging()

    products = load_products(PRODUCT_PATH)

    if not products:
        print("没有可用的商品数据，程序结束")
        return 

    if args.command == "search":
        results = filter_products(
            products=products,
            name=args.name,
            category=args.category,
            max_price=args.max_price,
        )

        show_products(
            results,
            args.name,
            args.category,
            args.max_price,
        )
        return

    if args.command == "add":
        new_product = Product(
            id=None,
            name=args.name,
            category=[args.category],
            price=args.price,
            rating=None,
            rating_count=0,
            store="命令行添加",
        )

        products = add_product(products, new_product)
        save_products(PRODUCT_PATH, products)

        print(f"商品 {new_product.name!r} 添加成功")
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