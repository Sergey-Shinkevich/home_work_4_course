from src.product import Product


def test_product_init(test_product_1: Product) -> None:
    """Тест инициализации класса Product"""
    assert test_product_1.name == "Имя"
    assert test_product_1.description == "Описание"
    assert test_product_1.price == 100
    assert test_product_1.quantity == 10
