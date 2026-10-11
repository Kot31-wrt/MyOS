# Архитектура ОС

## 1. Состав модулей

- **db.py** — соединение с SQLite и инициализация схемы.
- **syscalls.py** — системные вызовы и их логирование.
- **shell.py** — командная оболочка.
- **fs.py** — операции с файлами и каталогами.
- **auth.py** — проверка логина и пароля, хэширование SHA-256.
- **users.py** — управление пользователями и их ролями.
- **perms.py** — проверка прав доступа к файлам.
- **logging.py** — запись вызовов в syscalls_log.

## 2. Системные вызовы

### Список вызовов

- sys_login(login: str, password: str) -> bool
- sys_logout() -> bool
- sys_whoami() -> str
- sys_create_file(path: str, content: str) -> int
- sys_read_file(path: str) -> str
- sys_write_file(path: str, content: str) -> bool
- sys_delete_file(path: str) -> bool
- sys_copy_file(src: str, dst: str) -> bool
- sys_rename(old: str, new: str) -> bool
- sys_mkdir(path: str) -> bool
- sys_rmdir(path: str) -> bool
- sys_list_files(path: str) -> list
- sys_find(pattern: str) -> list
- sys_chmod(path: str, mode: str) -> bool
- sys_chown(path: str, owner: str) -> bool
- sys_useradd(login: str, password: str, role: str) -> bool
- sys_userdel(login: str) -> bool
- sys_backup(dest: str) -> bool
- sys_logs(limit: int) -> list
- sys_shutdown() -> bool

### Контракты вызовов

#### sys_create_file

- Предварительное условие: пользователь авторизован; путь указывает
  в каталог, где у пользователя есть право на запись.
- Постусловие: файл создан, возвращён его id.
- Побочный эффект: запись в syscalls_log.

#### sys_read_file

- Предварительное условие: пользователь авторизован; файл существует;
  у пользователя есть право на чтение.
- Постусловие: возвращено содержимое файла в виде строки.
- Побочный эффект: запись в syscalls_log.

#### sys_delete_file

- Предварительное условие: пользователь авторизован; файл существует;
  у пользователя есть право на удаление.
- Постусловие: файл помечен как удалённый (или удалён из таблицы
  files), возвращено true.
- Побочный эффект: запись в syscalls_log.

## 3. Структуры данных

### Пользователь (user)

    user = {
        'id': 1,
        'login': 'admin',
        'password_hash': 'abc123...',
        'role': 'admin',
        'created_at': '2025-01-01 10:00:00'
    }

### Файл или каталог (file)

    file = {
        'id': 1,
        'path': '/home/test.txt',
        'content': 'hello',
        'owner_id': 1,
        'created_at': '2025-01-01 10:00:00'
    }

### Процесс (process)

    process = {
        'id': 1,
        'name': 'shell',
        'state': 'running',
        'owner_id': 1,
        'memory_kb': 120,
        'created_at': '2025-01-01 10:00:00'
    }

### Запись журнала (log)

    log = {
        'id': 1,
        'call_name': 'sys_login',
        'args': 'admin',
        'user_id': 1,
        'status': 'OK',
        'created_at': '2025-01-01 10:00:00'
    }