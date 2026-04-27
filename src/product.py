class Product:
    """Объявление класса продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Конструктор класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict) -> 'Product':
        """Метод создания экземпляров класса"""
        return cls(**data)


    @property
    def price(self) -> float:
        """Геттер атрибута price"""
        return self.__price


    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер атрибута price"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price




