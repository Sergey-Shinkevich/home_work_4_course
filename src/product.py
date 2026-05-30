from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Объявление абстрактного класса продукта"""

    @abstractmethod
    def __add__(self, another: Any) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data: dict) -> Any:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass


class MixinREPR:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> None:
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', '{self.price}', '{self.quantity}')"


class Product(MixinREPR, BaseProduct):
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
        super().__init__()

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

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Конструктор подкласса Smartphone"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Product) -> float:
        if type(other) is Smartphone:
            result = (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
        return result


class LawnGrass(Product):
    """Объявление подкласса LawnGrass"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Конструктор подкласса LawnGrass"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: Product) -> float:
        if type(other) is LawnGrass:
            result = (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
        return result
