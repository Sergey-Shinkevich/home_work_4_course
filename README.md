# Домашняя работа по четвертому курсу. Урок 1.
____
Тема: Разработка интернет магазина
____
## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone [https://github.com/Sergey-Shinkevich/home_work_4_course] (https://github.com/Sergey-Shinkevich/home_work_4_course)
2. Установите зависимости через Poetry:
   ```bash
   poetry install
3. Для запуска тестов и генерации отчета о покрытии:
   ```bash
   pytest --cov=src

____
## Зависимости основные
- Python 3.14.2
____
## Зависимости для разработки
- Black 26.3.1
- Flake8 7.3.0
- Isort 8.0.1
- Mypy 1.20.0
- Pytest 9.0.3 
- Pytest-Cov 7.1.0
____
## Покрытие тестами
```
Name                     Stmts   Miss  Cover
--------------------------------------------
src\__init__.py              0      0   100%
src\category.py             19      0   100%
src\product.py              17      0   100%
src\utils.py                19      8    58%
tests\__init__.py            0      0   100%
tests\conftest.py            5      0   100%
tests\test_category.py      30      0   100%
tests\test_product.py       26      0   100%
tests\test_utils.py         16      0   100%
--------------------------------------------
TOTAL                      132      8    94%

