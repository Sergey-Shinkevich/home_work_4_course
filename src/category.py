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

    def add_product(self, item: Product) -> None:
        """Метод добавления нового Product в Category"""
        self.__products.append(item)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер атрибута products"""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
