#!/usr/bin/env python3
"""
Atlas Ultimate Code Fixer - комплексне автоматичне виправлення всіх типів помилок
Запускає всі фіксери послідовно з коректним порядком виправлень
"""

import subprocess
import sys
import time
from pathlib import Path


def print_header(text):
    """Друкує заголовок у відформатованому вигляді."""
    print("\n" + "=" * 70)
    print(f"🚀 {text}")
    print("=" * 70)


def run_fixer(script_name, description):
    """Запускає скрипт виправлення та обробляє результат."""
    print_header(f"{description}")

    start_time = time.time()
    # Запускаємо дочірній процес з небуферизованим виводом (-u),
    # щоб бачити прогрес в реальному часі.
    # Вивід буде напряму йти в термінал.
    result = subprocess.run(
        ["python", "-u", f"scripts/{script_name}"],
        text=True,
        check=False,  # Не кидати виключення при помилці
    )
    end_time = time.time()

    if result.returncode != 0:
        print(
            f"🔥 Скрипт {script_name} завершився з помилкою (код: {result.returncode})."
        )

    print(f"\nВиконано за {end_time - start_time:.2f} секунд")

    return result.returncode == 0


def run_ruff_check():
    """Запускає перевірку Ruff і показує статистику помилок."""
    print_header("Аналіз залишкових помилок")

    # Запускаємо ruff check з статистикою
    subprocess.run(["ruff", "check", "--statistics"], check=False)


def main():
    """Головна функція скрипту."""
    print_header("Atlas Ultimate Code Fixer 1.0")

    # Перевіряємо, чи ми в правильній директорії
    if not Path("pyproject.toml").exists():
        print("❌ Запустіть скрипт з кореневої директорії проєкту Atlas")
        sys.exit(1)

    # Крок 1: Виправлення імпортів (F821, F401, E402)
    run_fixer("quick_imports_fixer.py", "Крок 1/3: Виправлення імпортів")

    # Крок 2: Виправлення шаблонів коду (SIM102, SIM117, B904, SIM105, E722)
    run_fixer("quick_pattern_fixer.py", "Крок 2/3: Виправлення шаблонів коду")

    # Крок 3: Загальний фіксер для всіх інших типів помилок
    run_fixer("atlas_code_fixer.py", "Крок 3/3: Фінальний аналіз та виправлення")

    # Крок 4: Форматування коду
    print_header("Форматування коду")
    subprocess.run(["ruff", "format", "."], check=False)

    # Крок 5: Аналіз залишкових помилок
    run_ruff_check()

    # Налаштування pre-commit
    print_header("Налаштування pre-commit хуків")
    subprocess.run(["pre-commit", "install"], check=False)

    print_header("Готово! Код став краще 🎉")
    print("""
Залишкові помилки можна виправити наступними способами:
1. Виправити вручну, керуючись звітом вище
2. Використати AI асистента (Continue) у VS Code
3. Додати нові шаблони виправлень у відповідні фіксери
    """)


if __name__ == "__main__":
    main()
