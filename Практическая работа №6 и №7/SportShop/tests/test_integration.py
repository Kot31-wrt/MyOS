import unittest
import os

from src.cart import add_to_cart, cart_total
from src.orders import create_order, save_orders, load_orders
from src.storage import load_products


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.products = load_products('data/products.json')
        self.cart = []
        self.orders_file = 'data/test_orders.json'

    def tearDown(self):
        """Удаляет тестовый файл после каждого теста."""
        if os.path.exists(self.orders_file):
            os.remove(self.orders_file)

    def test_full_cycle(self):
        """Полный цикл: загрузка → корзина → заказ → сохранение → загрузка."""
        # 1. Загрузка товаров
        self.assertGreater(len(self.products), 0, "Товары не загрузились")

        # 2. Добавляем товар в корзину
        # Размер в JSON — строка, поэтому передаём "36.0"
        result, msg = add_to_cart(self.cart, self.products, 1, "36.0", 1)
        self.assertTrue(result, msg)
        self.assertEqual(len(self.cart), 1)

        # 3. Создаём заказ
        order = create_order(self.cart, 'Тестовый клиент', self.products)
        self.assertIn('name', order['items'][0])
        self.assertIsNotNone(order)
        self.assertGreater(order['total'], 0)

        # 4. Сохраняем заказ
        save_orders([order], self.orders_file)
        self.assertTrue(os.path.exists(self.orders_file))

        # 5. Загружаем заказ
        loaded = load_orders(self.orders_file)
        self.assertEqual(len(loaded), 1)

        # 6. Сумма совпадает
        self.assertEqual(loaded[0]['total'], order['total'])

    def test_cart_total_matches_order_total(self):
        """Сумма корзины совпадает с суммой заказа."""
        add_to_cart(self.cart, self.products, 1, "36.0", 1)
        add_to_cart(self.cart, self.products, 2, "37.0", 2)

        cart_sum = cart_total(self.cart)
        order = create_order(self.cart, 'Клиент', self.products)

        self.assertEqual(order['total'], cart_sum)

    def test_empty_cart_creates_no_order(self):
        """Пустая корзина — заказ не создаётся."""
        order = create_order(self.cart, 'Клиент', self.products)
        self.assertIsNone(order)

    def test_save_and_load_multiple_orders(self):
        """Сохранение и загрузка нескольких заказов."""
        add_to_cart(self.cart, self.products, 1, "36.0", 1)
        order1 = create_order(self.cart, 'Клиент 1', self.products)

        self.cart = []
        add_to_cart(self.cart, self.products, 2, "37.0", 2)
        order2 = create_order(self.cart, 'Клиент 2', self.products)

        save_orders([order1, order2], self.orders_file)
        loaded = load_orders(self.orders_file)

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]['client'], 'Клиент 1')
        self.assertEqual(loaded[1]['client'], 'Клиент 2')


if __name__ == '__main__':
    unittest.main()