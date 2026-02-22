class Product:
    """Класс для представления продукта."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict):
        """Создает новый экземпляр продукта из словаря."""
        return cls(data['name'], data['description'], data['price'], data['quantity'])

    @property
    def price(self) -> float:
        """Возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Устанавливает новую цену с проверкой и подтверждением."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirmation = input("Цена понижается. Вы уверены? (y/n): ")
            if confirmation.lower() != 'y':
                return

        self.__price = new_price
