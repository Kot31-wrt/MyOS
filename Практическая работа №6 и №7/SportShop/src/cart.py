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


def remove_from_cart(cart, product_id, size):
    """Удаляет позицию из корзины по id и размеру.

    Возвращает True, если позиция найдена и удалена.
    """
    for i, item in enumerate(cart):
        if item['id'] == product_id and item['size'] == size:
            del cart[i]
            return True
    return False


def update_quantity(cart, products, product_id, size, new_qty):
    """Меняет количество товара в корзине.

    Проверяет наличие на складе. Возвращает True, если изменено.
    """
    product = None
    for p in products:
        if p['id'] == product_id:
            product = p
            break

    if product is None:
        return False

    if size not in product['sizes']:
        return False

    if product['sizes'][size] < new_qty:
        return False

    for item in cart:
        if item['id'] == product_id and item['size'] == size:
            item['quantity'] = new_qty
            return True
    return False


def cart_total(cart):
    """Итоговая сумма корзины."""
    return sum(item['price'] * item['quantity'] for item in cart)