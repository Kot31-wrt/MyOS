from .db import init_db
from .syscalls import sys_echo, sys_get_users


BANNER = r"""
==========================================
  Учебная ОС: файловая система на SQLite
  Версия 0.1 (Day 1 prototype)
  Введите 'help' для списка команд.
==========================================
"""


HELP_TEXT = """Доступные команды:
  help          — показать эту справку
  echo <текст>  — вывести текст через системный вызов sys_echo
  users         — показать список пользователей (sys_get_users)
  exit          — завершить работу оболочки
"""


def handle_command(line: str) -> bool:
    """Обрабатывает одну строку команды.

    Возвращает False, если оболочку нужно завершить.
    """
    parts = line.strip().split(maxsplit=1)
    if not parts:
        return True

    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if cmd == "help":
        print(HELP_TEXT)

    elif cmd == "echo":
        if not arg:
            print("Использование: echo <текст>")
        else:
            print(sys_echo(arg))

    elif cmd == "users":
        users = sys_get_users()
        if not users:
            print("Список пользователей пуст.")
        else:
            print(f"{'ID':<4}{'Логин':<20}{'Роль':<12}{'Создан'}")
            for u in users:
                print(f"{u['id']:<4}{u['login']:<20}{u['role']:<12}{u['created_at']}")

    elif cmd == "exit":
        print("Завершение работы оболочки.")
        return False

    else:
        print(f"Неизвестная команда: {cmd}. Введите 'help'.")

    return True


def main() -> None:
    """Точка входа оболочки."""
    init_db()          # на случай, если БД ещё не создана
    print(BANNER)

    while True:
        try:
            line = input("os> ")
        except (EOFError, KeyboardInterrupt):
            print("\nЗавершение работы оболочки.")
            break

        if not handle_command(line):
            break


if __name__ == "__main__":
    main()