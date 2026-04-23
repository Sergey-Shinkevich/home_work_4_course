from src.category import Category
from src.product import Product


def test_category() -> None:
    """Тест инициализации класса Category и переменных класса"""
    product_1 = Product("Имя_1", "Описание_1", 100, 1)
    product_2 = Product("Имя_2", "Описание_2", 102, 2)
    category_1 = Category("Категория_1", "Описание_1", [product_1, product_2])
    assert category_1.name == "Категория_1"
    assert category_1.description == "Описание_1"
    assert len(category_1.products) == 2
    assert category_1.category_count == 1
    assert Category.category_count == 1
    assert category_1.product_count == 2
    assert Category.product_count == 2
    product_3 = Product("Имя_3", "Описание_3", 103, 3)
    category_2 = Category("Категория_2", "Описание_2", [product_3])
    assert Category.category_count == 2
    assert Category.product_count == 3
