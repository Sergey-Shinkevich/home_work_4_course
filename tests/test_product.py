import pytest

from src.product import Product


def test_product_init(test_product_1: Product) -> None:
    """Тест инициализации класса Product"""
    assert test_product_1.name == "Имя"
    assert test_product_1.description == "Описание"
    assert test_product_1.price == 100
    assert test_product_1.quantity == 10


def test_new_product() -> None:
    """Тест работы метода добавления нового продукта"""
    data = {"name": "name", "description": "description", "price": 100, "quantity": 10}
    expected_output = Product.new_product(data)

    assert expected_output.name == "name"
    assert expected_output.description == "description"
    assert expected_output.price == 100
    assert expected_output.quantity == 10


def test_getter_price() -> None:
    """Тест геттера цены"""
    data = {"name": "name", "description": "description", "price": 100, "quantity": 10}
    expected_output = Product.new_product(data)

    assert expected_output.price == 100


def test_setter_price() -> None:
    """Тест сеттера цены"""
    data = {"name": "name", "description": "description", "price": 100, "quantity": 10}
    expected_output = Product.new_product(data)
    expected_output.price = 500
    assert expected_output.price == 500

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        expected_output.price = 0

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        expected_output.price = -500


def test_str(test_product_1: Product) -> None:
    """Тест описания, метод __str__"""
    expected_output = "Имя, 100 руб. Остаток: 10 шт."
    assert str(test_product_1) == expected_output


def test_magic_add_method() -> None:
    """тест сложения сумм продуктов умноженное на их количество"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    expected_output = 2580000
    assert product1 + product2 == expected_output
