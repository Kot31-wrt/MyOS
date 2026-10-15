# Hotfix: cart_total

## Проблема

В ветке main отсутствовала функция cart_total, которая должна считать итоговую сумму корзины. Без неё нельзя корректно оформить заказ: сумма считалась бы неверно или программа падала бы с ошибкой.

## Что сделано

Добавлена функция cart_total в shop.py:

    def cart_total(cart):
        return sum(item['price'] * item['quantity'] for item in cart)

Функция суммирует произведение цены и количества для всех товаров в корзине и возвращает итоговую сумму заказа.

## Процесс исправления

1. Создана ветка hotfix/cart-total от main:

       git checkout main
       git checkout -b hotfix/cart-total

2. В shop.py добавлена функция cart_total, сделан коммит:

       git add shop.py
       git commit -m "Hotfix: добавлена функция cart_total"

3. Hotfix слит в main:

       git checkout main
       git merge hotfix/cart-total

4. Hotfix слит в develop, чтобы исправление не потерялось при следующем релизе:

       git checkout develop
       git merge hotfix/cart-total

## Конфликт при слиянии в develop

При слиянии hotfix/cart-total в develop возник конфликт: обе ветки изменяли конец файла shop.py.

В develop уже были функции get_low_stock и total_sum, а в hotfix добавлялась функция cart_total. Git не смог автоматически объединить изменения и оставил маркеры конфликта:

    <<<<<<< HEAD
    def total_sum(products):
        return sum(p['price'] * p['quantity'] for p in products)
    =======
    def cart_total(cart):
        return sum(item['price'] * item['quantity'] for item in cart)
    >>>>>>> hotfix/cart-total

## Как конфликт был разрешён

В VS Code выбрана команда «Принять оба изменения» — это сохранило обе функции: и total_sum, и cart_total. Маркеры конфликта удалены вручную.

После этого:

    git add shop.py
    git commit -m "Разрешён конфликт при слиянии hotfix/cart-total в develop"

## Проверка результата

В файле shop.py присутствуют обе функции:

    def total_sum(products):
        return sum(p['price'] * p['quantity'] for p in products)

    def cart_total(cart):
        return sum(item['price'] * item['quantity'] for item in cart)

Маркеров конфликта (<<<<<<<, =======, >>>>>>>) в файле не осталось.

История коммитов:

    git log --oneline --graph --all

Показывает слияние hotfix/cart-total и коммит с разрешением конфликта.

## Удаление ветки hotfix

После слияния ветка hotfix больше не нужна:

    git branch -d hotfix/cart-total

## Вывод

Hotfix — это срочное исправление критической ошибки в стабильной ветке main. В отличие от feature-веток, он создаётся от main, а не от develop, и сливается обратно в обе ветки, чтобы исправление не потерялось при следующем релизе.

При слиянии в develop возник конфликт, потому что develop и hotfix меняли один участок файла shop.py. Конфликт разрешён вручную: оставлены обе функции — и total_sum, и cart_total. Это корректное решение, так как обе функции нужны для работы проекта.