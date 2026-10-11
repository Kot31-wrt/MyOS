# MyOS — учебная ОС с файловой системой на SQLite

Прототип операционной системы, в котором файлы и каталоги хранятся
в базе данных SQLite.

## Запуск

    python -m venv .venv
    .venv\Scripts\activate
    python src/db.py
    python -m src.shell

## Команды

- help — справка
- echo <текст> — вывести текст
- users — список пользователей
- exit — выход

Полная документация — в docs/01_OS_Scope_and_NFR.md.
