import json
from datetime import datetime



# US-1. Товары с низким остатком
def get_low_stock(products):
    low = []
    for p in products:
        total = sum(p['sizes'].values())
        if total <= 3:
            low.append({**p, 'total': total})
    return sorted(low, key=lambda p: p['total'])



# US-2. Комбинированный поиск
def search_advanced(products, query, category=None,
                    min_price=None, max_price=None):
    result = []
    q = query.lower()
    for p in products:
        if q not in p['name'].lower():
            continue
        if category and p.get('category') != category:
            continue
        if min_price is not None and p['price'] < min_price:
            continue
        if max_price is not None and p['price'] > max_price:
            continue
        result.append(p)
    return result



# US-3. Аналитика по категориям
def count_by_category(products):
    """Словарь: категория → количество товаров."""
    result = {}
    for p in products:
        cat = p.get('category', 'без категории')
        result[cat] = result.get(cat, 0) + 1
    return dict(sorted(result.items(), key=lambda x: -x[1]))



# US-4. Сохранение заказов
def save_orders(orders, filename='orders.json'):
    """Сохраняет заказы в JSON. Если файл есть — добавляет к существующим."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing = []

    existing.extend(orders)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    return len(existing)



# Тестовые данные
if __name__ == "__main__":
    products = [
        {'id': 1, 'name': 'Air Max', 'price': 8990.0, 'category': 'кроссовки',
         'sizes': {36.0: 1, 37.0: 2}},
        {'id': 2, 'name': 'Superstar', 'price': 7490.0, 'category': 'кроссовки',
         'sizes': {37.0: 4, 38.0: 3}},
        {'id': 3, 'name': 'Runfalcon', 'price': 5590.0, 'category': 'кроссовки',
         'sizes': {39.0: 2}},
        {'id': 4, 'name': 'Футболка Adidas', 'price': 2990.0, 'category': 'одежда',
         'sizes': {'M': 5, 'L': 3}},
        {'id': 5, 'name': 'Мяч Nike', 'price': 1990.0, 'category': 'инвентарь',
         'sizes': {'стандарт': 10}},
    ]

    print("US-1. Товары с низким остатком:")
    for p in get_low_stock(products):
        print(f"  {p['name']} — {p['total']} шт.")

    print("\nUS-2. Поиск 'max':")
    for p in search_advanced(products, 'max'):
        print(f"  {p['name']} — {p['price']} руб.")

    print("\nUS-3. Аналитика по категориям:")
    for cat, count in count_by_category(products).items():
        print(f"  {cat}: {count}")

    print("\nUS-4. Сохранение заказа:")
    order = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'client': 'Иванов',
        'items': [{'name': 'Air Max', 'price': 8990.0, 'quantity': 1}],
    }
    total_orders = save_orders([order])
    print(f"  Всего заказов в файле: {total_orders}")

# СпортТовары — практическое занятие №7

def get_low_stock(products):
    low = []
    for p in products:
        total = sum(p['sizes'].values())
        if total <= 3:
            low.append({**p, 'total': total})
    return sorted(low, key=lambda p: p['total'])

def total_sum(products):
    return sum(p['price'] * p['quantity'] for p in products)

def cart_total(cart):
        return sum(item['price'] * item['quantity'] for item in cart)

def search_advanced(products, query, category=None,
                    min_price=None, max_price=None):
    result = []
    q = query.lower()
    for p in products:
        if q not in p['name'].lower():
            continue
        if category and p.get('category') != category:
            continue
        if min_price is not None and p['price'] < min_price:
            continue
        if max_price is not None and p['price'] > max_price:
            continue
        result.append(p)
    return result

def add_to_cart(cart, products, product_id, size, quantity):
    product = None
    for p in products:
        if p['id'] == product_id:
            product = p
            break

    if product is None:
        return False, "Товар не найден"

    if size not in product['sizes']:
        return False, f"Размер {size} недоступен"

    if product['sizes'][size] < quantity:
        return False, "Недостаточно товара на складе"

    for item in cart:
        if item['id'] == product_id and item['size'] == size:
            item['quantity'] += quantity
            return True, "Количество увеличено"

    cart.append({
        'id': product_id,
        'name': product['name'],
        'price': product['price'],
        'size': size,
        'quantity': quantity,
    })
    return True, "Товар добавлен"

def remove_from_cart(cart, name):
    cart[:] = [item for item in cart if item['name'] != name]


def update_quantity(cart, name, new_qty):
    for item in cart:
        if item['name'] == name:
            item['quantity'] = new_qty
            return True
    return False