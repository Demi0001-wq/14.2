from product import Product
from category import Category
from utils import load_data_from_json

if __name__ == "__main__":
    # Task 14.1 check
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.price)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name)
    print(len(category1.products.split('\n')) - 1)  # Number of lines
    print(Category.category_count)
    print(Category.product_count)

    # Task 14.2 check
    print("\nFormatted products:")
    print(category1.products)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(f"After add_product: {Category.product_count}")

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5
        }
    )
    print(f"New product: {new_product.name}")

    # Price setter
    print("\nSetting price to 800 (requires check if lowering):")
    # input required
    # new_product.price = 800

    print("Setting price to -100 (should fail):")
    new_product.price = -100
    print(f"Price: {new_product.price}")
