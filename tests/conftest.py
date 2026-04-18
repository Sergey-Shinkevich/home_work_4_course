import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def test_product_1() -> Product:
    """Данные для первого объекта класса Product"""
    return Product("Имя", "Описание", 100, 10)


@pytest.fixture
def test_product_2() -> Product:
    """Данные для второго объекта класса Product"""
    return Product("Имя2", "Описание2", 102, 12)

@pytest.fixture
def test_product_3() -> Product:
    """Данные для третьего объекта класса Product"""
    return Product("Имя3", "Описание3", 103, 13)

