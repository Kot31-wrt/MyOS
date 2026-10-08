from .db import get_connection


def log_syscall(call_name: str, args: str = "", user_id: int | None = None,
                status: str = "ok") -> None:
    """Записывает информацию о системном вызове в таблицу syscalls_log."""
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO syscalls_log (call_name, args, user_id, status) "
            "VALUES (?, ?, ?, ?);",
            (call_name, args, user_id, status),
        )
        conn.commit()
    finally:
        conn.close()


def sys_echo(message: str, user_id: int | None = None) -> str:
    """Возвращает переданное сообщение. Автоматически логируется."""
    log_syscall("sys_echo", args=message, user_id=user_id, status="ok")
    return message


def sys_get_users(user_id: int | None = None) -> list[dict]:
    """Возвращает список пользователей из базы. Автоматически логируется."""
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT id, login, role, created_at FROM users ORDER BY id;"
        ).fetchall()
        result = [dict(row) for row in rows]
    finally:
        conn.close()

    log_syscall("sys_get_users", args="", user_id=user_id, status="ok")
    return result