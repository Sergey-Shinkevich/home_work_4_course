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

    def __str__(self) -> str:
        """Переопределение метода пользовательского вывода объекта класса"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        """Метод сложения"""
        result = (self.__price * self.quantity) + (other.__price * other.quantity)
        return result

    @classmethod
    def new_product(cls, data: dict) -> "Product":
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
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Smartphone(Product):
    """Объявление подкласса Smartphone"""
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str) -> None:
        """Конструктор подкласса Smartphone"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Smartphone) -> float:
        if type(other) == Smartphone:
            result = (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
        return result


class LawnGrass(Product):
    """Объявление подкласса LawnGrass"""
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str) -> None:
        """Конструктор подкласса LawnGrass"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: LawnGrass) -> float:
        if type(other) == LawnGrass:
            result = (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
        return result



