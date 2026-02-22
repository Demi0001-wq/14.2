from product import Product


class Category:
    """Класс для представления категории продуктов."""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = []
        for product in products:
            self.add_product(product)

        Category.category_count += 1

    def add_product(self, product: Product):
        """Добавляет продукт в категорию и увеличивает общий счетчик продуктов."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку со списком продуктов в формате."""
        result = ""
        for product in self.__products:
            result += (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт.\n"
            )
        return result
