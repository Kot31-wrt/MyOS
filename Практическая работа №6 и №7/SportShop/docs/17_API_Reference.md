# API Reference — SportShop

Справочник по публичным функциям модулей `src/*.py`.

## Модуль src/catalog.py

### get_low_stock(products)

**Назначение:** возвращает список товаров с суммарным количеством ≤ 3.

**Параметры:**
- `products` (list[dict]) — список товаров.

**Возвращаемое значение:**
- `list[dict]` — список товаров с низким остатком. Каждый товар дополнен полем `total`. Отсортирован по возрастанию `total`.

**Пример:**
```python
low = get_low_stock(products)
for p in low:
    print(p['name'], p['total'])
```

**Исключения:**
- `KeyError` — если у товара нет поля `sizes`.



### search_advanced(products, query, category=None, min_price=None, max_price=None)

**Назначение:** комбинированный поиск товаров по названию, категории и диапазону цен.

**Параметры:**
- `products` (list[dict]) — список товаров.
- `query` (str) — подстрока для поиска в названии (без учёта регистра).
- `category` (str, optional) — фильтр по категории.
- `min_price` (float, optional) — минимальная цена.
- `max_price` (float, optional) — максимальная цена.

**Возвращаемое значение:**
- `list[dict]` — список товаров, удовлетворяющих всем условиям. Если ничего не найдено — пустой список.

**Пример:**
```python
result = search_advanced(products, 'max', category='кроссовки',
                         min_price=5000, max_price=10000)
for p in result:
    print(p['name'])
```

**Исключения:**
- `KeyError` — если у товара нет поля `name` или `price`.



### count_by_category(products)

**Назначение:** подсчитывает количество товаров в каждой категории.

**Параметры:**
- `products` (list[dict]) — список товаров.

**Возвращаемое значение:**
- `dict[str, int]` — словарь «категория → количество», отсортированный по убыванию количества. Товары без категории попадают в «без категории».

**Пример:**
```python
counts = count_by_category(products)
for cat, n in counts.items():
    print(cat, n)
```

**Исключения:**
- Не выбрасывает.



### avg_price(products)

**Назначение:** вычисляет среднюю цену товаров в каталоге.

**Параметры:**
- `products` (list[dict]) — список товаров.

**Возвращаемое значение:**
- `float` — средняя цена. Если список пуст — `0`.

**Пример:**
```python
print(avg_price(products))  # например, 6209.0
```

**Исключения:**
- `KeyError` — если у товара нет поля `price`.



## Модуль src/cart.py

### add_to_cart(cart, products, product_id, size, quantity)

**Назначение:** добавляет товар в корзину. Если такой товар с тем же размером уже есть — увеличивает количество.

**Параметры:**
- `cart` (list[dict]) — корзина.
- `products` (list[dict]) — каталог товаров.
- `product_id` (int) — id товара.
- `size` (str) — размер.
- `quantity` (int) — количество.

**Возвращаемое значение:**
- `tuple[bool, str]` — `(True, сообщение)` при успехе, `(False, сообщение)` при ошибке.

**Пример:**
```python
result, msg = add_to_cart(cart, products, 1, "36.0", 2)
if result:
    print("Товар добавлен:", msg)
```

**Исключения:**
- Не выбрасывает. Все ошибки возвращаются через `(False, сообщение)`.



### remove_from_cart(cart, product_id, size)

**Назначение:** удаляет позицию из корзины по id товара и размеру.

**Параметры:**
- `cart` (list[dict]) — корзина.
- `product_id` (int) — id товара.
- `size` (str) — размер.

**Возвращаемое значение:**
- `bool` — `True`, если позиция найдена и удалена, `False` — если не найдена.

**Пример:**
```python
if remove_from_cart(cart, 1, "36.0"):
    print("Удалено")
```

**Исключения:**
- Не выбрасывает.



### update_quantity(cart, products, product_id, size, new_qty)

**Назначение:** изменяет количество товара в корзине с проверкой наличия на складе.

**Параметры:**
- `cart` (list[dict]) — корзина.
- `products` (list[dict]) — каталог товаров.
- `product_id` (int) — id товара.
- `size` (str) — размер.
- `new_qty` (int) — новое количество.

**Возвращаемое значение:**
- `bool` — `True`, если количество изменено. `False` — если товар не найден, размер недоступен или недостаточно на складе.

**Пример:**
```python
update_quantity(cart, products, 1, "36.0", 5)
```

**Исключения:**
- Не выбрасывает.



### cart_total(cart)

**Назначение:** подсчитывает итоговую сумму корзины.

**Параметры:**
- `cart` (list[dict]) — корзина. Каждый элемент должен иметь поля `price` и `quantity`.

**Возвращаемое значение:**
- `float` — сумма `price × quantity` по всем позициям. `0` — если корзина пуста.

**Пример:**
```python
print(cart_total(cart))  # например, 23970.0
```

**Исключения:**
- `KeyError` — если у элемента нет `price` или `quantity`.



## Модуль src/orders.py

### create_order(cart, client_name, products)

**Назначение:** создаёт заказ из корзины.

**Параметры:**
- `cart` (list[dict]) — корзина.
- `client_name` (str) — имя клиента.
- `products` (list[dict]) — каталог товаров.

**Возвращаемое значение:**
- `dict` — заказ с полями `date`, `client`, `items`, `total`.
- `None` — если корзина пуста.

**Пример:**
```python
order = create_order(cart, 'Иванов', products)
if order:
    print(order['total'])
```

**Исключения:**
- Не выбрасывает.



### print_order(order)

**Назначение:** выводит заказ в консоль.

**Параметры:**
- `order` (dict) — заказ или `None`.

**Возвращаемое значение:**
- Нет (`None`).

**Пример:**
```python
print_order(order)
```

**Исключения:**
- Не выбрасывает. Если `order is None` — выводит «Заказ пуст».



### save_orders(orders, filename='orders.json')

**Назначение:** сохраняет заказы в JSON. Если файл существует — добавляет к существующим.

**Параметры:**
- `orders` (list[dict]) — список заказов.
- `filename` (str, optional) — путь к файлу. По умолчанию `orders.json`.

**Возвращаемое значение:**
- `int` — общее количество заказов в файле после сохранения.

**Пример:**
```python
total = save_orders([order], 'orders.json')
print(f"Всего заказов: {total}")
```

**Исключения:**
- `IOError` — при невозможности записи файла.



### load_orders(filename='orders.json')

**Назначение:** загружает заказы из JSON.

**Параметры:**
- `filename` (str, optional) — путь к файлу.

**Возвращаемое значение:**
- `list[dict]` — список заказов. Пустой список, если файла нет или он повреждён.

**Пример:**
```python
orders = load_orders('orders.json')
print(len(orders))
```

**Исключения:**
- Не выбрасывает. Ошибки чтения возвращаются пустым списком.



## Модуль src/analytics.py

### total_revenue(orders)

**Назначение:** считает общую сумму всех заказов.

**Параметры:**
- `orders` (list[dict]) — список заказов с полем `total`.

**Возвращаемое значение:**
- `float` — общая сумма.

**Пример:**
```python
print(total_revenue(orders))
```

**Исключения:**
- `KeyError` — если у заказа нет поля `total`.



### best_selling_product(orders)

**Назначение:** находит самый продаваемый товар по количеству.

**Параметры:**
- `orders` (list[dict]) — список заказов. Каждый содержит `items`.

**Возвращаемое значение:**
- `str` — название товара, или `None`, если заказов нет.

**Пример:**
```python
print(best_selling_product(orders))  # 'Air Max'
```

**Исключения:**
- Не выбрасывает.



### average_order_total(orders)

**Назначение:** вычисляет среднюю сумму заказа.

**Параметры:**
- `orders` (list[dict]) — список заказов.

**Возвращаемое значение:**
- `float` — средняя сумма. `0` — если заказов нет.

**Пример:**
```python
print(average_order_total(orders))
```

**Исключения:**
- `KeyError` — если у заказа нет поля `total`.



## Модуль src/storage.py

### load_products(filename='data/products.json')

**Назначение:** загружает товары из JSON.

**Параметры:**
- `filename` (str, optional) — путь к файлу.

**Возвращаемое значение:**
- `list[dict]` — список товаров. Пустой список, если файла нет или он повреждён.

**Пример:**
```python
products = load_products('data/products.json')
```

**Исключения:**
- Не выбрасывает.



### save_products(products, filename='data/products.json')

**Назначение:** сохраняет товары в JSON.

**Параметры:**
- `products` (list[dict]) — список товаров.
- `filename` (str, optional) — путь к файлу.

**Возвращаемое значение:**
- Нет (`None`).

**Пример:**
```python
save_products(products, 'data/products.json')
```

**Исключения:**
- `IOError` — при невозможности записи.

**Всего описано 17 функций.**