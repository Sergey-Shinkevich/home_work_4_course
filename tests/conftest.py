import pytest

from src.product import Product


@pytest.fixture
def test_product_1() -> Product:
    """Данные для первого объекта класса Product"""
    return Product("Имя", "Описание", 100, 10)
