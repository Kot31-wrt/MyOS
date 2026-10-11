import sqlite3
from pathlib import Path

# Путь к файлу базы данных
DB_DIR = Path(__file__).resolve().parent.parent / "db"
DB_PATH = DB_DIR / "os.sqlite"


def get_connection() -> sqlite3.Connection:
    """Возвращает соединение с базой данных.

    Каталог db/ создаётся автоматически, если его нет.
    """
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db() -> None:
    """Создаёт четыре таблицы, если они ещё не существуют."""
    conn = get_connection()
    cur = conn.cursor()

    # Таблица пользователей
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            login       TEXT    NOT NULL UNIQUE,
            password_hash TEXT  NOT NULL,
            role        TEXT    NOT NULL DEFAULT 'user',
            created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
        );
    """)

    # Таблица процессов
    cur.execute("""
        CREATE TABLE IF NOT EXISTS processes (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            state       TEXT    NOT NULL DEFAULT 'new',
            owner_id    INTEGER,
            memory_kb   INTEGER NOT NULL DEFAULT 0,
            created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (owner_id) REFERENCES users(id)
        );
    """)

    # Таблица файлов
    cur.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            path        TEXT    NOT NULL UNIQUE,
            content     TEXT    NOT NULL DEFAULT '',
            owner_id    INTEGER,
            created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (owner_id) REFERENCES users(id)
        );
    """)

    # Таблица журнала системных вызовов
    cur.execute("""
        CREATE TABLE IF NOT EXISTS syscalls_log (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            call_name   TEXT    NOT NULL,
            args        TEXT    NOT NULL DEFAULT '',
            user_id     INTEGER,
            status      TEXT    NOT NULL DEFAULT 'ok',
            created_at  TEXT    NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"База данных инициализирована: {DB_PATH}")