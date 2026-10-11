from src.db import init_db
from src.syscalls import (
    sys_echo, sys_get_users,
    sys_login, sys_logout, sys_whoami,
    sys_create_file, sys_list_files, sys_logs,
    sys_ps
)


BANNER = r"""
==========================================
  Учебная ОС: файловая система на SQLite
  Версия 0.2
  Введите 'help' для списка команд.
==========================================
"""


HELP_TEXT = """Доступные команды:
  help            — показать эту справку
  echo <текст>    — вывести текст через sys_echo
  users           — показать список пользователей (sys_get_users)
  whoami          — показать текущего пользователя (sys_whoami)
  login           — войти в систему (sys_login)
  logout          — выйти из системы (sys_logout)
  create          — создать файл (sys_create_file)
  ls              — список файлов (sys_list_files)
  ps              — список процессов (sys_ps)
  logs            — последние записи журнала (sys_logs)
  exit            — завершить работу оболочки
"""


def handle_command(line: str, current_user: str) -> tuple[bool, str]:
    """Обрабатывает одну строку команды.

    Возвращает (продолжать_работу, текущий_пользователь).
    """
    parts = line.strip().split(maxsplit=1)
    if not parts:
        return True, current_user

    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if cmd == "help":
        print(HELP_TEXT)

    elif cmd == "echo":
        if not arg:
            print("Использование: echo <текст>")
        else:
            print(sys_echo(arg, current_user))

    elif cmd == "users":
        users = sys_get_users(current_user)
        if not users:
            print("Список пользователей пуст.")
        else:
            print(f"{'ID':<4}{'Логин':<20}{'Роль':<12}{'Создан'}")
            for u in users:
                print(f"{u['id']:<4}{u['login']:<20}{u['role']:<12}{u['created_at']}")

    elif cmd == "whoami":
        print(sys_whoami(current_user))

    elif cmd == "login":
        login = input("Логин: ")
        password = input("Пароль: ")
        if sys_login(login, password, current_user):
            current_user = login
            print(f"Вы вошли как {login}")
        else:
            print("Ошибка входа")

    elif cmd == "logout":
        sys_logout(current_user)
        current_user = "guest"
        print("Вы вышли из системы.")

    elif cmd == "create":
        path = input("Путь: ")
        content = input("Содержимое: ")
        fid = sys_create_file(path, content, current_user)
        print(f"Создан файл с id={fid}")

    elif cmd == "ls":
        files = sys_list_files("/", current_user)
        if not files:
            print("(пусто)")
        else:
            for f in files:
                print(f)

    elif cmd == "ps":
        processes = sys_ps(current_user)
        if not processes:
            print("(процессов нет)")
        else:
            for p in processes:
                print(p)

    elif cmd == "logs":
        entries = sys_logs(10, current_user)
        if not entries:
            print("Журнал пуст.")
        else:
            for e in entries:
                print(e)

    elif cmd == "exit":
        print("Завершение работы оболочки.")
        return False, current_user

    else:
        print(f"Неизвестная команда: {cmd}. Введите 'help'.")

    return True, current_user


def main() -> None:
    """Точка входа оболочки."""
    init_db()
    print(BANNER)

    current_user = "guest"

    while True:
        try:
            line = input(f"{current_user}@myos:~$ ")
        except (EOFError, KeyboardInterrupt):
            print("\nЗавершение работы оболочки.")
            break

        keep_going, current_user = handle_command(line, current_user)
        if not keep_going:
            break


if __name__ == "__main__":
    main()