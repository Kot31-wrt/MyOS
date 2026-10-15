from src.catalog import get_low_stock, search_advanced, count_by_category
from src.cart import add_to_cart, remove_from_cart, update_quantity, cart_total
from src.orders import create_order, print_order, save_orders, load_orders
from src.analytics import total_revenue, best_selling_product, average_order_total
from src.storage import load_products


def main():
    products = load_products('data/products.json')
    if not products:
        print("Нет товаров. Проверьте data/products.json")
        return

    print("=== SportShop ===")
    print(f"Товаров в каталоге: {len(products)}")

    print("\nТовары с низким остатком:")
    for p in get_low_stock(products):
        print(f"  {p['name']} — {p['total']} шт.")

    print("\nПоиск 'max':")
    for p in search_advanced(products, 'max'):
        print(f"  {p['name']} — {p['price']} руб.")

    print("\nАналитика по категориям:")
    for cat, count in count_by_category(products).items():
        print(f"  {cat}: {count}")

    # Корзина
    cart = []
    add_to_cart(cart, products, 1, "36.0", 1)
    add_to_cart(cart, products, 2, "37.0", 2)
    print(f"\nКорзина: {len(cart)} позиций, сумма {cart_total(cart)} руб.")

    # Заказ
    order = create_order(cart, 'Иванов', products)
    print_order(order)

    if order:
        save_orders([order])
        print("Заказ сохранён в orders.json.")


if __name__ == "__main__":
    main()