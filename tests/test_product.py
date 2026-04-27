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

    expected_output.price = 0
    assert expected_output.price == 500

    expected_output.price = -500
    assert expected_output.price == 500
