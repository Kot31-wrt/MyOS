# История коммитов

## Вывод git log --oneline --graph --all

* 447735f (HEAD -> develop, origin/develop) Добавлено описание hotfix
*   58fe091 Разрешён конфликт при слиянии hotfix/cart-total в develop
|\  
* | 843107b Добавлено описание разрешения конфликта
| | *   f76e254 (origin/main, origin/HEAD, main) Разрешён конфликт при слиянии hotfix/cart-total
| | |\  
| | |/  
| |/|   
| * | 564a6e6 Hotfix: исправлена функция cart_total
| | * 2e82a29 Добавлена функция cart_total (с ошибкой)
| |/  
| | * 87f2726 (origin/feature/search-advanced, feature/search-advanced) Добавлено описание Pull Request
| | * 248e85b US-2: добавлена функция search_advanced
| |/  
|/|   
* |   eb995c7 Разрешён конфликт в total_sum
|\ \  
| * | fa126e1 (feature/total-v2) total_sum с учётом количества
* | | 3cbabe5 (feature/total-v1) total_sum без учёта количества
|/ /  
* / 125374a US-1: добавлена функция get_low_stock
|/  

## Анализ графа

### Сколько веток было создано?

Создано 7 веток:

- main — стабильная версия продукта;
- develop — ветка интеграции;
- feature/low-stock — функция get_low_stock;
- feature/total-v1 — total_sum без учёта количества;
- feature/total-v2 — total_sum с учётом количества;
- feature/search-advanced — функция search_advanced;
- hotfix/cart-total — срочное исправление функции cart_total.

### Какие слияния произошли?

1. feature/low-stock → develop — без конфликта.
2. feature/total-v1 → develop — без конфликта.
3. feature/total-v2 → develop — с конфликтом (обе ветки меняли total_sum).
4. hotfix/cart-total → main — без конфликта.
5. hotfix/cart-total → develop — с конфликтом (develop и hotfix меняли конец shop.py).

### Был ли конфликт и как он разрешён?

Да, было два конфликта слияния.

**Конфликт 1: feature/total-v2 → develop (коммит eb995c7).**

Обе ветки изменяли функцию total_sum:

- feature/total-v1 — сумма без учёта количества;
- feature/total-v2 — сумма с учётом количества.

Конфликт разрешён вручную: оставлена версия из feature/total-v2 (с учётом количества), так как она корректнее.

**Конфликт 2: hotfix/cart-total → develop (коммиты 58fe091 и f76e254).**

В develop уже были функции get_low_stock и total_sum. В hotfix добавлялась функция cart_total. Обе ветки меняли конец файла shop.py.

Конфликт разрешён вручную в VS Code командой «Принять оба изменения» — сохранены обе функции: total_sum и cart_total. Маркеры конфликта удалены, файл сохранён.

После разрешения:

    git add shop.py
    git commit -m "Разрешён конфликт при слиянии hotfix/cart-total в develop"

## Вывод

В ходе работы освоены:

- создание и переключение веток;
- слияние feature-веток в develop;
- создание и разрешение конфликтов слияния;
- hotfix — срочное исправление в main;
- имитация Pull Request;
- визуализация истории через git log --graph.

Ветвление позволяет разрабатывать функции изолированно и не ломать основную ветку. Конфликты — нормальная часть работы с Git; главное — правильно их разрешить.