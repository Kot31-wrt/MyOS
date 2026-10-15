import subprocess
import sys
import os


def check_python_version():
    """Проверяет, что версия Python не ниже 3.10."""
    if sys.version_info < (3, 10):
        print("Ошибка: требуется Python 3.10 или выше.")
        print(f"У вас: Python {sys.version.split()[0]}")
        sys.exit(1)
    print(f"[1/4] Python {sys.version.split()[0]} — OK")


def check_data():
    """Проверяет наличие файла data/products.json."""
    path = os.path.join("data", "products.json")
    if not os.path.exists(path):
        print(f"Ошибка: файл данных не найден: {path}")
        print("Создайте data/products.json с товарами.")
        sys.exit(1)
    print(f"[2/4] Файл данных найден: {path} — OK")


def run_tests():
    """Запускает все тесты из папки tests."""
    print("[3/4] Запуск тестов...")
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode != 0:
        print("Ошибка: тесты не прошли.")
        sys.exit(1)
    print("Тесты прошли успешно.")


def run_app():
    """Запускает main.py."""
    print("[4/4] Запуск приложения main.py...")
    print("-" * 50)
    subprocess.run([sys.executable, "main.py"])
    print("-" * 50)


if __name__ == "__main__":
    print("=" * 50)
    print("Сборка SportShop")
    print("=" * 50)
    check_python_version()
    check_data()
    run_tests()
    print("\nСборка успешна!\n")
    run_app()