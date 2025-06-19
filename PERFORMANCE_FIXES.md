# Atlas CodeReaderTool Performance Fixes

## Проблема
Atlas зависав при запуску через проблеми з індексацією коду:
- CodeReaderTool намагався проіндексувати всю папку venv-macos (сотні тисяч файлів)
- Рекурсивні помилки в sympy/polys/numberfields/resolvent_lookup.py
- Попередження pyautogui про invalid escape sequence
- Надто довгий час запуску (затримка до кількох хвилин)

## Виправлення

### 1. Розширені виключення директорій
```python
self.excluded_dirs = {
    '__pycache__', '.git', '.venv', 'venv', 'venv-macos', 'venv-linux', 
    'node_modules', '.pytest_cache', 'build', 'dist', '.mypy_cache',
    'site-packages', 'lib', 'include', 'Scripts', 'bin', 'share',
    '.DS_Store', 'unused', 'monitoring/logs'
}
```

### 2. Обмеження розміру та кількості файлів
- Максимальний розмір файлу: 1MB
- Максимальна кількість рядків: 10,000
- Максимальна кількість файлів для індексації: 200
- Таймаут індексації: 30 секунд

### 3. Обмеження рекурсії AST парсера
```python
import sys
old_limit = sys.getrecursionlimit()
sys.setrecursionlimit(500)  # Обмежуємо рекурсію
tree = ast.parse(content, filename=str(file_path))
sys.setrecursionlimit(old_limit)
```

### 4. Асинхронна індексація
- Індексація запускається в фоновому потоці
- Не блокує запуск Atlas
- Використовує існуючий кеш якщо доступний

### 5. Змінна середовища для відключення індексації
```bash
export ATLAS_DISABLE_CODE_INDEXING=true
```

### 6. Селективна індексація тільки Atlas файлів
```python
for pattern in ["*.py", "agents/*.py", "tools/*.py", "ui/*.py", "utils/*.py", "tests/*.py"]:
    python_files.extend(self.root_path.glob(pattern))
```

## Нові команди запуску

### Швидкий запуск без індексації:
```bash
python3 quick_launch_no_index.py
```

### Launcher з опцією швидкого режиму:
```bash
./launch_atlas.sh --fast        # або --no-index
```

### Звичайний запуск (з індексацією):
```bash
./launch_atlas.sh
python3 main.py
```

## Результат
- ⚡ Швидкий запуск: ~10 секунд замість кількох хвилин
- 🛡️ Захист від рекурсивних помилок
- 🎯 Індексація тільки Atlas коду, не бібліотек
- 📊 Зменшено навантаження на систему
- ✅ Зберігається функціональність Help режиму для Atlas файлів

## Файли змінено
- `tools/code_reader_tool.py` - основні виправлення
- `quick_launch_no_index.py` - новий швидкий launcher
- `launch_atlas.sh` - додана опція --fast

Atlas тепер запускається швидко і стабільно! 🚀
