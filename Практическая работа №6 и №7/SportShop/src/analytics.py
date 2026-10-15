def total_revenue(orders):
    """Общая сумма всех заказов."""
    return sum(order['total'] for order in orders)


def best_selling_product(orders):
    """Самый продаваемый товар (по количеству)."""
    counts = {}
    for order in orders:
        for item in order['items']:
            counts[item['name']] = counts.get(item['name'], 0) + item['quantity']
    if not counts:
        return None
    return max(counts, key=counts.get)


def average_order_total(orders):
    """Средняя сумма заказа."""
    if not orders:
        return 0
    return total_revenue(orders) / len(orders)