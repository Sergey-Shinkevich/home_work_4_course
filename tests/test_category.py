from src.category import Category
from src.product import Product


def test_category() -> None:
    """Тест инициализации класса Category и переменных класса"""
    product_1 = Product("Имя_1", "Описание_1", 100, 1)
    product_2 = Product("Имя_2", "Описание_2", 102, 2)
    category_1 = Category("Категория_1", "Описание_1", [product_1, product_2])

    assert category_1.name == "Категория_1"
    assert category_1.description == "Описание_1"
    assert category_1.product_count == 2
    assert category_1.category_count == 1
    assert Category.category_count == 1
    assert category_1.product_count == 2

    product_3 = Product("Имя_3", "Описание_3", 103, 3)
    category_2 = Category("Категория_2", "Описание_2", [product_3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_products_getter() -> None:
    """Тест работы геттера products"""
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Gray mirror", 180000.0, 5)
    category = Category("Smartphones", "Modern smartphones", [product])
    expected_output = "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."

    assert category.products == expected_output


def test_add_product() -> None:
    """Тест метода добавления продукта в категории"""
    Category.category_count = 0
    Category.product_count = 0
    product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Gray mirror", 180000.0, 5)
    product_2 = Product("Iphone", "Modern smartphone", 200000, 10)
    category_3 = Category("Smartphones", "Modern smartphones", [product_1])
    assert category_3.product_count == 1
    category_3.add_product(product_2)
    assert category_3.product_count == 2
