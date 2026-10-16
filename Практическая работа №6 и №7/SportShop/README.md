# СпортТовары — система управления магазином

## Описание

Учебный проект «СпортТовары» — приложение для управления магазином спортивных товаров. Позволяет вести каталог, работать с корзиной, оформлять заказы и строить аналитику по продажам.

Проект создан в рамках учебной практики УП.02 (специальность 09.02.07).

## Требования

- Python 3.10 или выше
- Стандартные библиотеки: `json`, `os`, `unittest`, `subprocess`
- SQLite не используется (данные хранятся в JSON)

## Установка

    git clone https://github.com/Kot31-wrt/MyOS.git
    cd "Практическая работа №6 и №7/SportShop"

## Запуск

    python main.py

## Тестирование

    python -m unittest discover -s tests

## Сборка

    python build.py

Скрипт сборки проверяет версию Python, наличие файла данных, запускает тесты и приложение.

## Структура проекта

    SportShop/
    ├── src/
    │   ├── __init__.py
    │   ├── catalog.py
    │   ├── cart.py
    │   ├── orders.py
    │   ├── analytics.py
    │   └── storage.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_catalog.py
    │   ├── test_cart.py
    │   ├── test_orders.py
    │   ├── test_analytics.py
    │   └── test_integration.py
    ├── docs/
    ├── data/
    │   └── products.json
    ├── main.py
    ├── build.py
    └── README.md

## Авторы

Студент: Муталибова Алина Руслановна
Группа: 3-ИП-7-24