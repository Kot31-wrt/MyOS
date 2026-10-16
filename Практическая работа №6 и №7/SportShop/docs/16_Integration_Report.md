# Отчёт об интеграции

## Общая информация

- Проект: SportShop
- Студент: Муталибова Алина Руслановна
- Группа: 3-ИП-7-24
- Дата: 16.10.2025

## Какие модули были выделены

Монолитный файл shop.py разбит на пять модулей в папке src/:

1. **src/catalog.py** — работа с каталогом товаров:
   - get_low_stock(products);
   - search_advanced(products, query, category, min_price, max_price);
   - count_by_category(products);
   - avg_price(products).

2. **src/cart.py** — работа с корзиной:
   - add_to_cart(cart, products, product_id, size, quantity);
   - remove_from_cart(cart, product_id, size);
   - update_quantity(cart, products, product_id, size, new_qty);
   - cart_total(cart).

3. **src/orders.py** — работа с заказами:
   - create_order(cart, client_name, products);
   - print_order(order);
   - save_orders(orders, filename);
   - load_orders(filename).

4. **src/analytics.py** — аналитика по заказам:
   - total_revenue(orders);
   - best_selling_product(orders);
   - average_order_total(orders).

5. **src/storage.py** — работа с JSON-файлами:
   - load_products(filename);
   - save_products(products, filename).

## Какие импорты используются

**В main.py:**

    from src.catalog import get_low_stock, search_advanced, count_by_category
    from src.cart import add_to_cart, cart_total
    from src.orders import create_order, print_order, save_orders
    from src.analytics import total_revenue, best_selling_product
    from src.storage import load_products

**В src/orders.py:**

    import json
    from datetime import datetime

**В src/storage.py:**

    import json
    import os

**В tests/test_integration.py:**

    from src.cart import add_to_cart, cart_total
    from src.orders import create_order, save_orders, load_orders
    from src.storage import load_products

## Какие интеграционные тесты написаны

Файл tests/test_integration.py содержит 4 теста:

1. **test_full_cycle** — полный цикл: загрузка товаров → добавление в корзину → создание заказа → сохранение в JSON → загрузка обратно → проверка суммы.

2. **test_cart_total_matches_order_total** — сумма корзины совпадает с суммой заказа.

3. **test_empty_cart_creates_no_order** — пустая корзина не создаёт заказ.

4. **test_save_and_load_multiple_orders** — сохранение и загрузка нескольких заказов.

Эти тесты проверяют взаимодействие модулей cart, orders, storage и обнаруживают несовместимости, которые не видны при модульном тестировании.

## Какие ошибки были найдены и исправлены

В ходе работы специально была внесена ошибка в src/cart.py: ключ 'name' заменён на 'product'.

**Как проявилась ошибка:**

Интеграционный тест test_full_cycle упал с ошибкой:

    AssertionError: 'name' not found in {'id': 1, 'product': 'Air Max',
    'price': 8990.0, 'size': '36.0', 'quantity': 1}

Тест проверял, что в элементе заказа есть ключ 'name'. После внесения ошибки ключ стал 'product', и проверка не прошла.

**Как была исправлена:**

1. Открыт файл src/cart.py.
2. Найдена строка с ключом 'product'.
3. Ключ заменён обратно на 'name'.
4. Тесты перезапущены — все прошли.

Подробнее — в docs/15_Integration_Errors.md.

## Как работает скрипт сборки

Файл build.py выполняет четыре шага:

1. **check_python_version()** — проверяет, что версия Python не ниже 3.10.
2. **check_data()** — проверяет наличие файла data/products.json.
3. **run_tests()** — запускает все тесты из папки tests через unittest discover.
4. **run_app()** — запускает main.py.

Запуск:

    python build.py

Скрипт останавливается на первой же ошибке: не та версия Python, нет файла данных или упали тесты — приложение не запускается.