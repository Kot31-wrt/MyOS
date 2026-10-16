# Руководство разработчика — SportShop

## 1. Настройка окружения

### Требования

- Python 3.10 или выше
- Git
- VS Code (рекомендуется)
- Стандартные библиотеки Python: `json`, `os`, `unittest`, `subprocess`

### Клонирование репозитория

    git clone https://github.com/Kot31-wrt/MyOS.git
    cd "Практическая работа №6 и №7/SportShop"

### Создание виртуального окружения

    python -m venv .venv
    .venv\Scripts\activate

### Проверка версии Python

    python --version

Должно быть 3.10 или выше.



## 2. Запуск тестов

### Все тесты

    python -m unittest discover -s tests

### Конкретный файл

    python -m unittest tests.test_integration

### Конкретный тест

    python -m unittest tests.test_integration.TestIntegration.test_full_cycle

### Ожидаемый результат

    ....
    -
    Ran 4 tests in 0.005s

    OK

Если хоть один тест упал — сборка прервётся.



## 3. Как добавить новую функцию

### Шаг 1. Определите модуль

Новая функция должна логически принадлежать одному из существующих модулей:

| Модуль | Для чего |
|||
| `src/catalog.py` | работа с каталогом товаров |
| `src/cart.py` | корзина |
| `src/orders.py` | заказы |
| `src/analytics.py` | аналитика |
| `src/storage.py` | сохранение / загрузка JSON |

### Шаг 2. Добавьте функцию с docstring

Пример новой функции в `src/catalog.py`:

```python
def expensive_products(products, min_price=10000):
    """Возвращает товары дороже указанной цены.

    Параметры:
        products (list[dict]) — список товаров.
        min_price (float) — минимальная цена.

    Возвращает:
        list[dict] — список товаров дороже min_price.
    """
    return [p for p in products if p['price'] > min_price]
```

### Шаг 3. Напишите тесты

Создайте файл `tests/test_catalog.py` (или допишите в существующий):

```python
import unittest
from src.catalog import expensive_products


class TestExpensiveProducts(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(expensive_products([]), [])

    def test_filters_by_price(self):
        products = [
            {'name': 'A', 'price': 5000},
            {'name': 'B', 'price': 15000},
        ]
        result = expensive_products(products, 10000)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'B')


if __name__ == '__main__':
    unittest.main()
```

### Шаг 4. Запустите тесты

    python -m unittest discover -s tests

Все тесты должны пройти.

### Шаг 5. Запустите сборку

    python build.py

### Шаг 6. Закоммитьте

    git add .
    git commit -m "Добавлена функция expensive_products"
    git push



## 4. Как создать новую ветку и сделать PR

### Шаг 1. Убедитесь, что вы в develop

    git checkout develop
    git pull

### Шаг 2. Создайте feature-ветку

    git checkout -b feature/expensive-products

### Шаг 3. Внесите изменения

Добавьте функцию в `src/catalog.py`, тесты в `tests/test_catalog.py`. Сохраните (`Ctrl+S`).

### Шаг 4. Закоммитьте

    git add .
    git commit -m "US-N: добавлена функция expensive_products"

### Шаг 5. Отправьте ветку

    git push -u origin feature/expensive-products

### Шаг 6. Создайте Pull Request

1. Откройте репозиторий на GitHub.
2. Появится кнопка **Compare & pull request**.
3. Нажмите.
4. Заполните:
   - **Что сделано:** добавлена функция `expensive_products`.
   - **Как проверить:** `python -m unittest tests.test_catalog`.
   - **Связанные задачи:** US-N.
5. Нажмите **Create pull request**.

### Шаг 7. Слияние

После проверки:

    git checkout develop
    git merge feature/expensive-products
    git branch -d feature/expensive-products
    git push



## 5. Как запустить сборку

### Обычный запуск

    python build.py

### Что делает build.py

1. **check_python_version()** — проверяет версию Python (3.10+).
2. **check_data()** — проверяет наличие `data/products.json`.
3. **run_tests()** — запускает все тесты.
4. **run_app()** — запускает `main.py`.

Скрипт останавливается на первой же ошибке.

### Ожидаемый вывод

    ==================================================
    Сборка SportShop
    ==================================================
    [1/4] Python 3.15.0 — OK
    [2/4] Файл данных найден: data\products.json — OK
    [3/4] Запуск тестов...
    ....
    -
    Ran 4 tests in 0.005s

    OK
    Тесты прошли успешно.

    Сборка успешна!

    [4/4] Запуск приложения main.py...
    --
    === SportShop ===
    ...
    --



## 6. Развёртывание

Приложение не требует:

- сервера базы данных;
- специализированного ПО;
- установки зависимостей через `pip`.

Достаточно:

- Python 3.10+;
- файла `data/products.json`;
- папки `src/` с модулями.

Запуск: `python main.py`.



## 9. Полезные команды

|              Команда                   |              Что делает            |
|                                        |                                    |
|           `python main.py`             |            Запуск приложения       |
|           `python build.py`            | Сборка (проверки + тесты + запуск) |
| `python -m unittest discover -s tests` |                Все тесты           |
|             `git status`               |           Текущее состояние git    |
|             `git branch`               |               Список веток         |
|       `git log --oneline --graph`      |             История коммитов       |