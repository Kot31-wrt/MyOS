import unittest
from shop import (
    get_low_stock, search_advanced, total_sum, cart_total,
    add_to_cart, remove_from_cart, update_quantity,
)


# Тесты для get_low_stock
class TestGetLowStock(unittest.TestCase):

    def test_empty_list(self):
        """Пустой список — пустой результат."""
        self.assertEqual(get_low_stock([]), [])

    def test_no_low_stock(self):
        """Товары с достаточным остатком не попадают в результат."""
        products = [{'name': 'A', 'sizes': {40: 10}}]
        self.assertEqual(get_low_stock(products), [])

    def test_one_low_stock(self):
        """Только товар с остатком ≤ 3 попадает в результат."""
        products = [
            {'name': 'A', 'sizes': {40: 1}},
            {'name': 'B', 'sizes': {40: 10}},
        ]
        result = get_low_stock(products)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'A')

    def test_sorted_by_total(self):
        """Результат отсортирован по возрастанию total."""
        products = [
            {'name': 'A', 'sizes': {40: 3}},
            {'name': 'B', 'sizes': {40: 1}},
            {'name': 'C', 'sizes': {40: 2}},
        ]
        result = get_low_stock(products)
        totals = [p['total'] for p in result]
        self.assertEqual(totals, sorted(totals))


# Тесты для search_advanced
class TestSearchAdvanced(unittest.TestCase):

    def setUp(self):
        """Общие тестовые данные для всех тестов класса."""
        self.products = [
            {'name': 'Air Max', 'price': 8990.0, 'category': 'кроссовки'},
            {'name': 'Superstar', 'price': 7490.0, 'category': 'кроссовки'},
            {'name': 'Футболка', 'price': 2990.0, 'category': 'одежда'},
            {'name': 'Мяч Nike', 'price': 1990.0, 'category': 'инвентарь'},
        ]

    def test_search_by_name(self):
        """Поиск по подстроке в названии."""
        result = search_advanced(self.products, 'max')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Air Max')

    def test_search_case_insensitive(self):
        """Поиск не зависит от регистра."""
        result = search_advanced(self.products, 'MAX')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Air Max')

    def test_search_by_category(self):
        """Фильтр по категории."""
        result = search_advanced(self.products, 's', category='кроссовки')
        names = [p['name'] for p in result]
        self.assertIn('Superstar', names)
        self.assertNotIn('Футболка', names)

    def test_search_by_price_range(self):
        """Фильтр по диапазону цен."""
        result = search_advanced(self.products, '', min_price=1500, max_price=5000)
        names = [p['name'] for p in result]
        self.assertIn('Футболка', names)
        self.assertIn('Мяч Nike', names)
        self.assertNotIn('Air Max', names)

    def test_search_not_found(self):
        """Ничего не найдено — пустой список."""
        result = search_advanced(self.products, 'zzz')
        self.assertEqual(result, [])


# Тесты для total_sum
class TestTotalSum(unittest.TestCase):

    def test_empty_cart(self):
        """Пустая корзина — сумма 0."""
        self.assertEqual(total_sum([]), 0)

    def test_single_item(self):
        """Один товар: цена × количество."""
        cart = [{'name': 'A', 'price': 1000.0, 'quantity': 2}]
        self.assertEqual(total_sum(cart), 2000.0)

    def test_multiple_items(self):
        """Несколько товаров — сумма складывается."""
        cart = [
            {'name': 'A', 'price': 1000.0, 'quantity': 2},
            {'name': 'B', 'price': 500.0, 'quantity': 3},
        ]
        self.assertEqual(total_sum(cart), 3500.0)


# Тесты для add_to_cart
class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.products = [
            {'id': 1, 'name': 'A', 'price': 1000.0, 'sizes': {40: 5, 41: 2}},
            {'id': 2, 'name': 'B', 'price': 2000.0, 'sizes': {40: 10}},
        ]

    def test_invalid_size(self):
        """Несуществующий размер — ошибка."""
        cart = []
        result, message = add_to_cart(cart, self.products, 1, 99, 1)
        self.assertFalse(result)
        self.assertIn('размер', message.lower())

    def test_product_not_found(self):
        """Несуществующий товар — ошибка."""
        cart = []
        result, message = add_to_cart(cart, self.products, 999, 40, 1)
        self.assertFalse(result)
        self.assertIn('найден', message.lower())

    def test_success(self):
        """Успешное добавление товара."""
        cart = []
        result, message = add_to_cart(cart, self.products, 1, 40, 2)
        self.assertTrue(result)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]['quantity'], 2)

    def test_insufficient_stock(self):
        """Недостаточно товара — ошибка."""
        cart = []
        result, message = add_to_cart(cart, self.products, 1, 41, 100)
        self.assertFalse(result)


# Проверка деления на ноль
class TestExpectedErrors(unittest.TestCase):
    def test_division_by_zero(self):
        """Проверка, что деление на ноль вызывает ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0


# Тесты для корзины
class TestCart(unittest.TestCase):

    def setUp(self):
        self.products = [
            {'id': 1, 'name': 'Air Max',   'price': 8990.0, 'sizes': {40: 5, 41: 3}},
            {'id': 2, 'name': 'Superstar', 'price': 7490.0, 'sizes': {40: 10, 41: 4}},
            {'id': 3, 'name': 'Runfalcon', 'price': 5590.0, 'sizes': {42: 2}},
        ]

    # add_to_cart

    def test_add_to_cart_success(self):
        """Успешное добавление товара в корзину."""
        cart = []
        result, message = add_to_cart(cart, self.products, 1, 40, 2)
        self.assertTrue(result)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]['name'], 'Air Max')
        self.assertEqual(cart[0]['quantity'], 2)
        self.assertEqual(cart[0]['size'], 40)

    def test_add_to_cart_twice_increases_quantity(self):
        """Повторное добавление увеличивает количество."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 2)
        add_to_cart(cart, self.products, 1, 40, 3)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]['quantity'], 5)

    def test_add_to_cart_different_sizes(self):
        """Один товар, разные размеры — две позиции."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 1)
        add_to_cart(cart, self.products, 1, 41, 1)
        self.assertEqual(len(cart), 2)

    # remove_from_cart

    def test_remove_from_cart(self):
        """Удаление позиции по имени."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 2)
        add_to_cart(cart, self.products, 2, 40, 1)
        self.assertEqual(len(cart), 2)

        remove_from_cart(cart, 'Air Max')
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]['name'], 'Superstar')

    def test_remove_nonexistent(self):
        """Удаление несуществующего товара ничего не меняет."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 1)
        remove_from_cart(cart, 'Несуществующий')
        self.assertEqual(len(cart), 1)

    # update_quantity

    def test_update_quantity(self):
        """Изменение количества товара."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 2)
        result = update_quantity(cart, 'Air Max', 5)
        self.assertTrue(result)
        self.assertEqual(cart[0]['quantity'], 5)

    def test_update_quantity_not_found(self):
        """Изменение количества несуществующего товара — False."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 2)
        result = update_quantity(cart, 'Несуществующий', 10)
        self.assertFalse(result)

    # cart_total

    def test_cart_total_empty(self):
        """Пустая корзина — сумма 0."""
        self.assertEqual(cart_total([]), 0)

    def test_cart_total_with_items(self):
        """Сумма по нескольким товарам."""
        cart = [
            {'name': 'A', 'price': 1000.0, 'quantity': 2},
            {'name': 'B', 'price': 500.0,  'quantity': 3},
        ]
        self.assertEqual(cart_total(cart), 3500.0)


if __name__ == '__main__':
    unittest.main()