from unittest.mock import patch, mock_open

from src.utils import load_json


def test_load_json_success() -> None:
    """Тест успешного чтения файла JSON"""
    mock_config = '{"name": "Samsung Galaxy C23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0, "quantity": 5}'
    with patch("builtins.open", mock_open(read_data=mock_config)):
        result = load_json("fake_path.json")
    assert result == {'description': '256GB, Серый цвет, 200MP камера', 'name': 'Samsung Galaxy C23 Ultra', 'price': 180000.0, 'quantity': 5}


def test_load_json_file_not_found() -> None:
    """Тест, когда файла нет"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_json("missing_path.json")
    assert result == []


def test_load_json_invalid_file() -> None:
    """Синтаксическая ошибка в файле"""
    mock_bad_config = '{"name": "Samsung Galaxy C23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0, "quantity": '  # Нет закрывающей скобки
    with patch("builtins.open", mock_open(read_data=mock_bad_config)):
        result = load_json("bad_path.json")
    assert result == []
