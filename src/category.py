from src.product import Product


class Category:
    """Объявление класса Category"""

    category_count = 0
    product_count = 0
    name: str
    description: str
    __products: list[Product]

    def __init__(self, name: str, description: str, products: list) -> None:
        """Конструктор класса Category"""
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(self.__products)
        Category.category_count += 1

    def __str__(self) -> str:
        """Переопределение пользовательского вывода экземпляра класса"""
        summ = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {summ} шт."

    def add_product(self, item: Product) -> None:
        """Метод добавления нового Product в Category"""
        if not isinstance(item, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(item)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер атрибута products"""
        results = []
        for product in self.__products:
            results.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(results)

    def middle_price(self) -> float:
        """Подсчитывает среднюю цену товара в категории"""
        try:
            result = sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            result = 0
        return result
