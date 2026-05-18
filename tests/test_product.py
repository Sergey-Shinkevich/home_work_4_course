import pytest

from src.product import LawnGrass, Product, Smartphone


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


def test_init_class_smartphones() -> None:
    """Тест инициализации подкласса Smartphones"""
    smartphone_1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    assert smartphone_1.name == "Iphone 15"
    assert smartphone_1.description == "512GB, Gray space"
    assert smartphone_1.price == 210000.0
    assert smartphone_1.quantity == 8
    assert smartphone_1.efficiency == 98.2
    assert smartphone_1.model == "15"
    assert smartphone_1.memory == 512
    assert smartphone_1.color == "Gray space"


def test_init_class_LawnGrass() -> None:
    """Тест инициализации подкласса LawnGrass"""
    grass_1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    assert grass_1.name == "Газонная трава"
    assert grass_1.description == "Элитная трава для газона"
    assert grass_1.price == 500
    assert grass_1.quantity == 20
    assert grass_1.country == "Россия"
    assert grass_1.germination_period == "7 дней"
    assert grass_1.color == "Зеленый"


def test_add_smartphones_normal() -> None:
    """Тест метод сложения объектов класса Smartphones"""
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    result = smartphone1 + smartphone2

    assert result == 2580000


def test_add_smartphones_error() -> None:
    """Тест стрессоустойчивости метода сложения объектов класса Smartphones"""
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    with pytest.raises(TypeError):
        print(smartphone1 + 1)


def test_add_LawnGrass_normal() -> None:
    """Тест метод сложения объектов класса LawnGrass"""
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    result = grass1 + grass2

    assert result == 16750


def test_add_LawnGrass_error() -> None:
    """Тест стрессоустойчивости метода сложения объектов класса LawnGrass"""
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        print(grass1 + 1)
