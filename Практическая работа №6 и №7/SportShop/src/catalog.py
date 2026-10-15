def get_low_stock(products):
    """Возвращает товары с суммарным количеством ≤ 3."""
    low = []
    for p in products:
        total = sum(p['sizes'].values())
        if total <= 3:
            low.append({**p, 'total': total})
    return sorted(low, key=lambda p: p['total'])


def search_advanced(products, query, category=None,
                    min_price=None, max_price=None):
    """Комбинированный поиск товаров."""
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


def count_by_category(products):
    """Словарь: категория → количество товаров."""
    result = {}
    for p in products:
        cat = p.get('category', 'без категории')
        result[cat] = result.get(cat, 0) + 1
    return dict(sorted(result.items(), key=lambda x: -x[1]))


def avg_price(products):
    """Средняя цена товаров."""
    if not products:
        return 0
    return sum(p['price'] for p in products) / len(products)