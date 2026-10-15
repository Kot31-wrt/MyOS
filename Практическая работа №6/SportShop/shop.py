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



