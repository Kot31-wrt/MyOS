print("Приложение Чудо Обувь запущено")
print("Добро пожаловать!")



login = "admin"
last_name = "Админов"
price = 8990.0
quantity = 5
in_stock = True

print("Логин:", login)
print("Фамилия:", last_name)
print("Цена:", price, ".руб")
print("Количество:", quantity)
print("В наличии:", in_stock)




sizes = [36.0, 37.0, 38.0, 39.0]
print("\nДоступные размеры:")
for s in sizes:
    print("-", s)




print("\nНомера по порядку:")
for i in range(len(sizes)):
    print(i + 1, "-", sizes[i])
if quantity <=3:
    print("\nМало на складе")
else:
    print("\nДостаточно на складе")




users = [
    {'login': 'admin', 'last_name': 'Админов', 'role': 'администатор'},
    {'login': 'manager', 'last_name': 'Менеджеров', 'role': 'менеджер'},
    {'login': 'user', 'last_name': 'Пользователев', 'role': 'авторизованный'}
]

for u in users: 
    print(f"Логин: {u['login']}, фамилия: {u['last_name']}, роль: {u['role']}")



products = [
    {'id': 1, 'name': 'Air Max', 'price': 8990.0, 'sizes': {36.0: 5, 37.0: 2}},
    {'id': 2, 'name': 'Superstar', 'price': 7490.0, 'sizes': {37.0: 4, 38.0: 3}},
    {'id': 3, 'name': 'Runfalcon', 'price': 5590.0, 'sizes': {39.0: 2}},
    {'id': 4, 'name': 'Ultraboost', 'price': 12990.0, 'sizes': {40.0: 3, 41.0: 4, 42.0: 2}},
    {'id': 5, 'name': 'Gazelle',    'price': 6490.0,  'sizes': {38.0: 6, 39.0: 1}},
]

for p in products:
    total_qty = sum(p['sizes'].values())
    print(f"{p['name']} — {p['price']} руб., всего на складе: {total_qty} шт.")



def find_user(login):
    for u in users:
        if u['login'] == login:
            return u
    return None

result = find_user('admin')
if result:
    print(f"Найден пользователь: {result['last_name']}")
else:
    print("Пользователь не найден")



def total_sum(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total

cart = [
    {'name': 'Air Max', 'price': 8990.0, 'quantity': 2},
    {'name': 'Superstar', 'price': 7490.0, 'quantity': 1},
]

print(f"Итоговая сумма заказа: {total_sum(cart)} руб.")


sorted_by_price = sorted(products, key=lambda p: p['price'])
print("\nТовары по возрастанию цены:")
for p in sorted_by_price:
    print(f"{p['name']} — {p['price']} руб.")



low_stock = [p for p in products if sum(p['sizes'].values()) <= 3]
print("\nТовары с низким остатком (≤ 3 шт.):")
for p in low_stock:
    print(p['name'])



def search_products(query):
    query = query.lower()
    return [p for p in products if query in p['name'].lower()]
found = search_products('max')
print("\nРезультаты поиска 'max':")
for p in found:
    print(p['name'])



def filter_by_price(products, min_price, max_price):
    return [p for p in products if min_price <= p['price'] <= max_price]

result = filter_by_price(products, 5000, 8000)
print("\nТовары от 5000 до 8000 руб.:")
for p in result:
    print(f"{p['name']} — {p['price']} руб.")



def add_to_cart(cart, product, size, quantity):
    cart.append({
        'product': product['name'],
        'price': product['price'],
        'size': size,
        'quantity': quantity
    })

def remove_from_cart(cart, name):
    cart[:] = [item for item in cart if item['product'] != name]

def change_quantity(cart, name, new_qty):
    for item in cart:
        if item['product'] == name:
            item['quantity'] = new_qty
            break

cart = []
add_to_cart(cart, products[0], 36.0, 2)
add_to_cart(cart, products[1], 37.0, 1)

print("\nКорзина:")
for item in cart:
    print(f"{item['product']}, размер {item['size']}, "
          f"{item['quantity']} шт. x {item['price']} = "
          f"{item['quantity'] * item['price']} руб.")

print(f"Итого: {total_sum(cart)} руб.")

change_quantity(cart, 'Air Max', 3)
remove_from_cart(cart, 'Superstar')

print("\nПосле изменений:")
for item in cart:
    print(f"{item['product']}, размер {item['size']}, {item['quantity']} шт.")
print(f"Итого: {total_sum(cart)} руб.")



# Задание 8. 
# 2. Функция get_sizes(product)
def get_sizes(product):
    return list(product['sizes'].keys())

#3. Функция get_total_quantity(product)
def get_total_quantity(product):
    return sum(product['sizes'].values())

# 4. Сортировка товаров по названию
sorted_by_name = sorted(products, key=lambda p: p['name'])
print("Товары по алфавиту:")
for p in sorted_by_name:
    print(f"  {p['name']} — {p['price']} руб.")

# 5. Фильтрация товаров дешевле 6000 руб.
cheap = [p for p in products if p['price'] < 6000]
print("\nТовары дешевле 6000 руб.:")
for p in cheap:
    print(f"  {p['name']} — {p['price']} руб.")

# 6. Вывод через while
print("\nВсе товары (цикл while):")
i = 0
while i < len(products):
    p = products[i]
    print(f"  {p['name']} — {p['price']} руб., всего: {get_total_quantity(p)} шт.")
    i += 1



#Задание 9. (Дополнительно)
# Список заказов
orders = [
    {
        'date': '2025-10-05',
        'client': 'Иванов',
        'items': [
            {'name': 'Air Max',   'price': 8990.0, 'quantity': 2},
            {'name': 'Gazelle',   'price': 6490.0, 'quantity': 1},
        ]
    },
    {
        'date': '2025-09-28',
        'client': 'Петрова',
        'items': [
            {'name': 'Runfalcon', 'price': 5590.0, 'quantity': 3},
        ]
    },
    {
        'date': '2025-10-12',
        'client': 'Сидоров',
        'items': [
            {'name': 'Ultraboost', 'price': 12990.0, 'quantity': 1},
            {'name': 'Superstar',  'price': 7490.0,  'quantity': 2},
            {'name': 'Air Max',    'price': 8990.0,  'quantity': 1},
        ]
    },
]

# Функция подсчёта суммы заказа
def order_total(order):
    total = 0
    for item in order['items']:
        total += item['price'] * item['quantity']
    return total

# Сортировка заказов по дате
sorted_orders = sorted(orders, key=lambda o: o['date'])

# Вывод всех заказов
print("Заказы, отсортированные по дате:")
print("=" * 50)

for order in sorted_orders:
    print(f"\nДата:   {order['date']}")
    print(f"Клиент: {order['client']}")
    print("Состав заказа:")
    for item in order['items']:
        line_total = item['price'] * item['quantity']
        print(f"  {item['name']}: {item['quantity']} шт. × "
              f"{item['price']} руб. = {line_total} руб.")
    print(f"Итого: {order_total(order)} руб.")
    print("-" * 50)