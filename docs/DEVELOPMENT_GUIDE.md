# Atlas Development Guidelines

## Архітектура розробки

Atlas розробляється з використанням подвійного підходу до середовищ розробки:

### 🐧 Основне середовище розробки (Linux)
- **Платформа**: Linux (Ubuntu/GitHub Codespaces)
- **Python**: 3.12
- **Призначення**: Розробка ядра, тестування, CI/CD
- **Особливості**: Headless-сумісність для хмарної розробки

### 🍎 Цільова платформа (macOS)
- **Платформа**: macOS (основна платформа для користувачів)
- **Python**: 3.13
- **Призначення**: Нативний macOS додаток
- **Особливості**: Повний GUI з нативною інтеграцією macOS

## Workflow розробки

### 1. Розробка на Linux (Python 3.12)
```bash
# Налаштування середовища розробки
python3.12 -m venv venv-dev
source venv-dev/bin/activate
pip install -r requirements-linux.txt

# Розробка та тестування
python main.py --headless --debug
python -m pytest tests/
```

### 2. Тестування на macOS (Python 3.13)
```bash
# Налаштування цільового середовища
python3.13 -m venv venv-macos
source venv-macos/bin/activate
pip install -r requirements-macos.txt

# Тестування нативних функцій
python main.py --platform-info
python main.py --debug
```

## Стандарти кодування

### Платформна сумісність
```python
# Використовуйте платформні утиліти
from utils.platform_utils import IS_MACOS, IS_LINUX, IS_HEADLESS

def screenshot_function():
    if IS_MACOS:
        # Використовуйте Quartz API
        return capture_with_quartz()
    elif IS_LINUX and not IS_HEADLESS:
        # Використовуйте PyAutoGUI
        return capture_with_pyautogui()
    else:
        # Fallback для headless
        return create_dummy_screenshot()
```

### Управління залежностями
```python
# Безпечний імпорт з fallback
try:
    import customtkinter as ctk
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False
    if not IS_HEADLESS:
        print("Warning: GUI not available")
```

### Конфігурація середовищ

#### requirements-linux.txt (Python 3.12)
```txt
# Базові залежності для розробки
customtkinter==5.2.2
# Без macOS-специфічних пакетів (pyobjc-*)
# Інструменти розробки
pytest>=7.0.0
black>=22.0.0
```

#### requirements-macos.txt (Python 3.13)
```txt
# Повний набір для macOS
customtkinter==5.2.2
pyobjc-core==11.1
pyobjc-framework-Quartz==11.1
pyobjc-framework-Cocoa==11.1
# macOS-оптимізовані версії
```

## Структура проекту

### Платформні модулі
```
utils/
├── platform_utils.py          # Детекція платформи
├── macos_utils.py             # macOS нативні функції
├── linux_utils.py             # Linux утиліти розробки
└── cross_platform.py          # Кросплатформенні функції

tools/
├── screenshot_tool.py          # Платформо-адаптивні скріншоти
├── automation_tool.py          # Кросплатформенна автоматизація
└── system_integration.py      # Системна інтеграція
```

### Конфігураційні файли
```
# Розробка (Linux)
config-dev.ini                 # Налаштування розробки
requirements-linux.txt         # Залежності Linux
launch_linux_dev.sh           # Скрипт запуску розробки

# Продакшн (macOS)
config-macos.ini               # Налаштування macOS
requirements-macos.txt         # Залежності macOS
launch_macos.sh               # Скрипт запуску macOS
```

## Процес розробки

### 1. Фаза розробки (Linux)
- Розробка основної логіки на Python 3.12
- Тестування в headless режимі
- Реалізація кросплатформенних функцій
- CI/CD pipeline тестування

### 2. Фаза адаптації (macOS)
- Тестування на Python 3.13
- Інтеграція нативних macOS функцій
- Оптимізація GUI для macOS
- Тестування користувацького досвіду

### 3. Інтеграційне тестування
```bash
# Linux testing
python3.12 main.py --headless --test-mode
python3.12 -m pytest tests/ -v

# macOS testing  
python3.13 main.py --platform-info
python3.13 main.py --gui-test
```

## Версіонування та релізи

### Стратегія релізів
1. **Dev builds**: Linux Python 3.12 (щоденні)
2. **Beta builds**: macOS Python 3.13 (тижневі)
3. **Release builds**: macOS-оптимізовані (місячні)

### Таггінг
```bash
# Development tags
git tag -a v1.0.0-dev-linux -m "Linux development build"

# Production tags
git tag -a v1.0.0-macos -m "macOS production release"
```

## Налагодження

### Linux Development
```bash
# Debug режим з повним логуванням
python main.py --debug --headless --log-level DEBUG

# Тестування без GUI
python main.py --cli --test-mode
```

### macOS Production
```bash
# Тестування нативних функцій
python main.py --debug --test-native

# Перевірка дозволів системи
python main.py --check-permissions
```

## Best Practices

### 1. Кросплатформенний код
- Завжди використовуйте `platform_utils` для детекції ОС
- Реалізуйте fallback механізми
- Тестуйте на обох платформах

### 2. Управління залежностями
- Підтримуйте окремі requirements файли
- Використовуйте version pinning для стабільності
- Документуйте платформні відмінності

### 3. Тестування
- Автоматизовані тести на Linux (CI/CD)
- Мануальне тестування на macOS
- Інтеграційні тести для кросплатформенності

Цей підхід забезпечує ефективну розробку на Linux з нативною оптимізацією для macOS.
