from src.product import Product

class Category:
    """Объявление класса Category"""
    category_count = 0
    product_count = 0
    name: str
    description: str
    products: list[Product]
    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(self.products)
