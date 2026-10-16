# Руководство пользователя — SportShop

## Что умеет приложение

SportShop — консольное приложение для управления магазином спортивных товаров. Позволяет:

- просматривать каталог товаров;
- искать товары по названию, категории и цене;
- находить товары с низким остатком;
- добавлять товары в корзину;
- оформлять заказы;
- сохранять и загружать заказы;
- строить аналитику по продажам.

## Требования

- Python 3.10 или выше.
- Файл `data/products.json` с товарами.

## Запуск

    python main.py

Приложение автоматически загружает товары и выполняет базовые операции.



## Сценарий 1. Просмотр каталога

**Что делает:** загружает список товаров из `data/products.json` и выводит их на экран.

**Команда:**

```python
from src.storage import load_products

products = load_products('data/products.json')
for p in products:
    print(p['name'], p['price'], p['category'])
```

**Ожидаемый результат:**

    Air Max 8990.0 кроссовки
    Superstar 7490.0 кроссовки
    Runfalcon 5590.0 кроссовки
    Футболка Adidas 2990.0 одежда
    Мяч Nike 1990.0 инвентарь



## Сценарий 2. Поиск товара

**Что делает:** ищет товары по подстроке в названии, категории и диапазону цен.

**Команда:**

```python
from src.catalog import search_advanced

# Поиск по названию
result = search_advanced(products, 'max')
for p in result:
    print(p['name'])

# Поиск по категории и цене
result = search_advanced(products, '', category='кроссовки',
                         min_price=5000, max_price=8000)
for p in result:
    print(p['name'], p['price'])
```

**Ожидаемый результат:**

    Air Max
    Superstar 7490.0



## Сценарий 3. Добавление в корзину

**Что делает:** добавляет товар в корзину по id, размеру и количеству.

**Команда:**

```python
from src.cart import add_to_cart, cart_total

cart = []
result, msg = add_to_cart(cart, products, 1, "36.0", 2)
print(result, msg)

result, msg = add_to_cart(cart, products, 2, "37.0", 1)
print(result, msg)

print("Сумма корзины:", cart_total(cart))
```

**Ожидаемый результат:**

    True Товар добавлен
    True Товар добавлен
    Сумма корзины: 25470.0

**Возможные ошибки:**

| Сообщение | Причина |
|||
| «Товар не найден» | Неверный id |
| «Размер 99 недоступен» | Такого размера нет |
| «Недостаточно товара на складе» | Запрошено больше, чем есть |



## Сценарий 4. Оформление заказа

**Что делает:** создаёт заказ из корзины, выводит его и сохраняет в JSON.

**Команда:**

```python
from src.orders import create_order, print_order, save_orders

order = create_order(cart, 'Иванов', products)
print_order(order)
save_orders([order], 'orders.json')
```

**Ожидаемый результат:**

    Заказ от 2026-10-16 для Иванов
      Air Max (размер 36.0): 2 шт. × 8990.0 руб.
      Superstar (размер 37.0): 1 шт. × 7490.0 руб.
    Итого: 25470.0 руб.
    Всего заказов в файле: 1

**Если корзина пуста:**

    order = create_order([], 'Иванов', products)
    print(order)   # None



## Сценарий 5. Просмотр аналитики

**Что делает:** считает общую выручку, средний чек и самый продаваемый товар.

**Команда:**

```python
from src.orders import load_orders
from src.analytics import total_revenue, average_order_total, best_selling_product

orders = load_orders('orders.json')

print("Общая выручка:", total_revenue(orders))
print("Средний чек:", average_order_total(orders))
print("Хит продаж:", best_selling_product(orders))
```

**Ожидаемый результат:**

    Общая выручка: 25470.0
    Средний чек: 25470.0
    Хит продаж: Air Max



## Сценарий 6. Сохранение и загрузка заказов

**Что делает:** сохраняет заказы в JSON и загружает их обратно.

**Команда:**

```python
from src.orders import save_orders, load_orders

# Сохранение
save_orders([order], 'orders.json')

# Загрузка
loaded = load_orders('orders.json')
print(f"Загружено заказов: {len(loaded)}")
for o in loaded:
    print(o['date'], o['client'], o['total'])
```

**Ожидаемый результат:**

    Загружено заказов: 1
    2026-10-16 Иванов 25470.0

**Если файла нет:**

    loaded = load_orders('несуществующий.json')
    print(loaded)   # []


## Полный пример работы

```python
from src.storage import load_products
from src.catalog import get_low_stock, search_advanced
from src.cart import add_to_cart, cart_total
from src.orders import create_order, print_order, save_orders, load_orders
from src.analytics import total_revenue, best_selling_product

# 1. Загрузка каталога
products = load_products('data/products.json')

# 2. Товары с низким остатком
print("Низкий остаток:")
for p in get_low_stock(products):
    print(f"  {p['name']} — {p['total']} шт.")

# 3. Поиск
print("\nПоиск 'max':")
for p in search_advanced(products, 'max'):
    print(f"  {p['name']} — {p['price']} руб.")

# 4. Корзина
cart = []
add_to_cart(cart, products, 1, "36.0", 1)
add_to_cart(cart, products, 2, "37.0", 2)
print(f"\nКорзина: {cart_total(cart)} руб.")

# 5. Заказ
order = create_order(cart, 'Иванов', products)
print_order(order)
save_orders([order])

# 6. Аналитика
orders = load_orders('orders.json')
print(f"\nВыручка: {total_revenue(orders)} руб.")
print(f"Хит продаж: {best_selling_product(orders)}")
```

**Ожидаемый результат:**

    Низкий остаток:
      Runfalcon — 2 шт.
      Air Max — 3 шт.

    Поиск 'max':
      Air Max — 8990.0 руб.

    Корзина: 23970.0 руб.
    Заказ от 2026-10-16 для Иванов
      Air Max (размер 36.0): 1 шт. × 8990.0 руб.
      Superstar (размер 37.0): 2 шт. × 7490.0 руб.
    Итого: 23970.0 руб.

    Выручка: 23970.0 руб.
    Хит продаж: Superstar