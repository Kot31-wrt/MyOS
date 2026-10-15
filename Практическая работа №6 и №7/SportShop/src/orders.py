import json
from datetime import datetime


def create_order(cart, client_name, products):
    """Создаёт заказ из корзины.

    Возвращает словарь заказа или None, если корзина пуста.
    """
    if not cart:
        return None

    return {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'client': client_name,
        'items': [dict(item) for item in cart],
        'total': sum(item['price'] * item['quantity'] for item in cart),
    }


def print_order(order):
    """Выводит заказ в консоль."""
    if order is None:
        print("Заказ пуст.")
        return
    print(f"Заказ от {order['date']} для {order['client']}")
    for item in order['items']:
        print(f"  {item['name']} (размер {item['size']}): "
              f"{item['quantity']} шт. × {item['price']} руб.")
    print(f"Итого: {order['total']} руб.")


def save_orders(orders, filename='orders.json'):
    """Сохраняет заказы в JSON."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing = []

    existing.extend(orders)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    return len(existing)


def load_orders(filename='orders.json'):
    """Загружает заказы из JSON."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []