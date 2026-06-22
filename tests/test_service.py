"""
Arrange-Act-Assert
"""


from product_app.models import Product
from product_app.service import (
    filter_products,
    sort_products_by_price,
    add_product
)
from product_app.repository import load_products,save_products
from product_app.main import create_parser
#====================================
# 生成测试集数据
#====================================
def make_products():
    return [
        Product(
            id=None,
            name="RTX-4090",
            category=["GPU", "NVIDIA-GPU"],
            price=9999.0,
        ),
        Product(
            id=None,
            name="iPhone-18-1TB",
            category=["Phone"],
            price=18000.0,
        ),
        Product(
            id = None,
            name = "D7",
            category = ["自行车"],
            price=2499.0,
        ),
    ]



#====================================
# 测试函数
#====================================


# 1. 按照product.name 筛选商品
def test_filter_products_by_name():

    products = make_products()

    results = filter_products(products,name = "4090")

    assert len(results) == 1
    assert results[0].name == "RTX-4090"



# 2. 按照product.category 筛选商品
def test_filter_products_by_category():
    
    products = make_products()

    results = filter_products(products, category="gpu")

    assert len(results) == 1
    assert results[0].name == "RTX-4090"



# 3. 按照product.price 筛选商品
def test_filter_products_by_max_price():

    products = make_products()

    results = filter_products(products, max_price=4000)

    assert len(results) == 1
    assert results[0].name == "D7"


# 4. 按照 product.name,product.category,product.price 筛选商品
def test_filter_products_by_name_category_and_price():
    
    products = make_products()

    results = filter_products(
        products,
        name="rtx",
        category="nvidia",
        max_price=10000,
    )

    assert len(results) == 1
    assert results[0].name == "RTX-4090"


# 5. 按照product.price 从低到高 筛选商品
def test_sort_products_by_price_ascending():

    products = make_products()

    results = sort_products_by_price(products)

    assert [product.name for product in results] == [
        "D7",
        "RTX-4090",
        "iPhone-18-1TB"
    ]


# 6. 按照product.price 从高到低 筛选商品
def test_sort_products_by_price_descending():

    products = make_products()

    results = sort_products_by_price(products,reverse=True)

    assert [product.name for product in results] == [
        "iPhone-18-1TB",
        "RTX-4090",
        "D7"
    ] 


# 7. 异常处理1 -> 找不到加载数据
def test_load_prodcuts_one(tmp_path):

    missing_file = tmp_path/"missing.json"

    results = load_products(missing_file)

    assert results == []

# 8. 异常处理2 -> 加载的数据json格式错误
def test_load_products_two(tmp_path):

    invalid_file = tmp_path / "products.json"
    invalid_file.write_text("{invalid json}",encoding= 'utf-8')

    results = load_products(invalid_file)

    assert results == []


# 9. add商品测试 
def test_add_product():

    products = make_products()

    new_product = Product(
        id = None,
        name = 'HUAWEI NOVA 15',
        category = ['phone'],
        price = 2049.0
    )

    original_count = len(products)

    results = add_product(products,new_product)

    assert len(results) == original_count + 1
    assert results[-1] == new_product


# 10. 保存并读取测试
def test_save_and_load_products(tmp_path):

    file_path = tmp_path / "products.json"

    products = [
        Product(
            id = 'test_001',
            name = 'HUAWEI NOVA 15',
            category = ['phone'],
            price = 2049.0
        )
    ]

    save_products(file_path,products)
    loaded_products = load_products(file_path)

    assert loaded_products == products 


# 11. search 参数解析测试
def test_create_parser_search_command():

    parser = create_parser()

    command_args = [
        "search",
        "--name",
        "4090",
        "--category",
        "gpu",
        "--max-price",
        "10000"
    ]

    args = parser.parse_args(command_args)

    assert args.command == "search"
    assert args.name == '4090'
    assert args.category == 'gpu'
    assert args.max_price == 10000



# 12. add 参数解析测试
def test_create_parser_add_command():

    parser = create_parser()

    command_args = [
        "add",
        "--name",
        "RTX-5090",
        "--category",
        "GPU",
        "--price",
        "15999"
    ]

    args = parser.parse_args(command_args)

    assert args.command == "add"
    assert args.name == 'RTX-5090'
    assert args.category == 'GPU'
    assert args.price == 15999
