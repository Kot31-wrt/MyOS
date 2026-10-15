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



