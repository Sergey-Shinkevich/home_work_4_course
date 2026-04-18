import json
from typing import Any

from src.category import Category
from src.product import Product


def load_json(path: str) -> Any:
    """Функция чтения JSON файла"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def create_objects(data: list) -> list:
    """Создание объектов из списка словарей"""
    categories = []
    for item in data:
        product_list = []
        for product in item["products"]:
            product_list.append(Product(**product))
        item["products"] = product_list
        categories.append(Category(**item))
    return categories
