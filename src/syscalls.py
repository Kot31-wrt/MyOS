from src.db import get_connection


def log_syscall(call_name: str, args: str = "",
                user_id: str = "system", status: str = "OK") -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO syscalls_log (call_name, args, user_id, status) "
        "VALUES (?, ?, ?, ?)",
        (call_name, args, user_id, status),
    )
    conn.commit()
    conn.close()


# Аутентификация 

def sys_login(login: str, password: str, current_user: str = "guest") -> bool:
    log_syscall("sys_login", login, current_user)
    return True


def sys_logout(current_user: str = "guest") -> bool:
    log_syscall("sys_logout", "", current_user)
    return True


def sys_whoami(current_user: str = "guest") -> str:
    log_syscall("sys_whoami", "", current_user)
    return current_user


# Файлы

def sys_create_file(path: str, content: str = "",
                    current_user: str = "guest") -> int:
    log_syscall("sys_create_file", path, current_user)
    return 1


def sys_read_file(path: str, current_user: str = "guest") -> str:
    log_syscall("sys_read_file", path, current_user)
    return ""


def sys_write_file(path: str, content: str,
                   current_user: str = "guest") -> bool:
    log_syscall("sys_write_file", path, current_user)
    return True


def sys_delete_file(path: str, current_user: str = "guest") -> bool:
    log_syscall("sys_delete_file", path, current_user)
    return True


def sys_copy_file(src: str, dst: str,
                  current_user: str = "guest") -> bool:
    log_syscall("sys_copy_file", f"{src} -> {dst}", current_user)
    return True


def sys_rename(old: str, new: str,
               current_user: str = "guest") -> bool:
    log_syscall("sys_rename", f"{old} -> {new}", current_user)
    return True


def sys_list_files(path: str, current_user: str = "guest") -> list:
    log_syscall("sys_list_files", path, current_user)
    return []


def sys_find(pattern: str, current_user: str = "guest") -> list:
    log_syscall("sys_find", pattern, current_user)
    return []


# Каталоги

def sys_mkdir(path: str, current_user: str = "guest") -> bool:
    log_syscall("sys_mkdir", path, current_user)
    return True


def sys_rmdir(path: str, current_user: str = "guest") -> bool:
    log_syscall("sys_rmdir", path, current_user)
    return True


# Права и пользователи

def sys_chmod(path: str, mode: str,
              current_user: str = "guest") -> bool:
    log_syscall("sys_chmod", f"{path} {mode}", current_user)
    return True


def sys_chown(path: str, owner: str,
              current_user: str = "guest") -> bool:
    log_syscall("sys_chown", f"{path} -> {owner}", current_user)
    return True


def sys_useradd(login: str, password: str, role: str = "user",
                current_user: str = "guest") -> bool:
    log_syscall("sys_useradd", login, current_user)
    return True


def sys_userdel(login: str, current_user: str = "guest") -> bool:
    log_syscall("sys_userdel", login, current_user)
    return True


# Обслуживание

def sys_backup(dest: str, current_user: str = "guest") -> bool:
    log_syscall("sys_backup", dest, current_user)
    return True


def sys_logs(limit: int = 10, current_user: str = "guest") -> list:
    log_syscall("sys_logs", str(limit), current_user)
    return []


def sys_shutdown(current_user: str = "guest") -> bool:
    log_syscall("sys_shutdown", "", current_user)
    return True

# Процессы

def sys_ps(current_user: str = "guest") -> list:
    log_syscall("sys_ps", "", current_user)
    return [] # Заглушка: процессов нет, возвращаем пустой список

def sys_echo(message: str, current_user: str = "guest") -> str:
    # Возвращает переданное сообщение
    log_syscall("sys_echo", message, current_user)
    return message

def sys_get_users(current_user: str = "guest") -> list:
    # Возвращает список пользователей из базы
    log_syscall("sys_get_users", "", current_user)
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT id, login, role, created_at FROM users ORDER BY id;"
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()

# Проверка

if __name__ == "__main__":
    print(sys_login("admin", "secret"))
    print(sys_whoami("admin"))
    print(sys_create_file("/test.txt", "hello", "admin"))
    print(sys_list_files("/", "admin"))