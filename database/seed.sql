-- insert 5 categories 
insert into categories (name,description)
VALUES 
	('GPU','图形处理器和显卡'),
	('CPU','中央处理器'),
	('Memory','计算机内存'),
	('Storage','固态硬盘和机械硬盘'),
	('Peripherals','键盘、鼠标和显示器');


-- insert 20 products

INSERT INTO products (
    name,
    category_id,
    price,
    stock,
    description
)
VALUES
    ('RTX-4090', 1, 12999.00, 5, 'NVIDIA 高性能显卡'),
    ('RTX-4070', 1, 4799.00, 12, 'NVIDIA 中高端显卡'),
    ('RX-7900-XTX', 1, 6999.00, 8, 'AMD 高性能显卡'),
    ('RX-7800-XT', 1, 4299.00, 10, 'AMD 中高端显卡'),
    ('Ryzen 9 7950X', 2, 3999.00, 7, 'AMD 旗舰处理器'),
    ('Ryzen 7 7800X3D', 2, 2899.00, 15, 'AMD 游戏处理器'),
    ('Intel Core i9-14900K', 2, 4299.00, 6, 'Intel 旗舰处理器'),
    ('Intel Core i7-14700K', 2, 2999.00, 11, 'Intel 高性能处理器'),
    ('Kingston Fury 32GB', 3, 699.00, 20, 'DDR5 32GB 内存'),
    ('Corsair Vengeance 32GB', 3, 749.00, 18, 'DDR5 32GB 内存'),
    ('Crucial 16GB', 3, 299.00, 30, 'DDR5 16GB 内存'),
    ('G.Skill Trident Z5 64GB', 3, 1499.00, 9, 'DDR5 64GB 内存'),
    ('Samsung 990 PRO 2TB', 4, 1299.00, 14, 'NVMe 固态硬盘'),
    ('WD Black SN850X 2TB', 4, 1199.00, 16, 'NVMe 固态硬盘'),
    ('Crucial P3 Plus 1TB', 4, 499.00, 25, 'NVMe 固态硬盘'),
    ('Seagate FireCuda 530 2TB', 4, 1399.00, 8, 'NVMe 固态硬盘'),
    ('Logitech G Pro X Mouse', 5, 899.00, 13, '无线游戏鼠标'),
    ('Razer DeathAdder V3', 5, 599.00, 17, '有线游戏鼠标'),
    ('Keychron Q1 Keyboard', 5, 1099.00, 10, '机械键盘'),
    ('Dell UltraSharp U2723QE', 5, 3999.00, 4, '27英寸显示器');