# 🍎 Atlas macOS - Що робити після першого запуску

## Виправлені проблеми ✅

З вашого логу видно, що:
- ✅ **Screenshot функціональність працює** (немає помилок Quartz)
- ✅ **Всі інструменти завантажилися** (24 built-in tools)
- ✅ **Gemini API працює** (successfully initialized)
- ✅ **GUI запустилася** на macOS

## Що потрібно налаштувати

### 1. API ключі
```bash
# Швидке налаштування
./setup_config_macos.sh

# Або відредагуйте config.ini вручну
nano config.ini
```

**OpenAI API** (опціонально):
- Отримайте ключ: https://platform.openai.com/account/api-keys
- Замініть `YOUR_API_KEY_HERE` в секції `[OpenAI]`

**Gemini API** вже працює, але якщо хочете оновити:
- Отримайте ключ: https://makersuite.google.com/app/apikey
- Оновіть в секції `[Gemini]`

### 2. Дозволи macOS
Надайте дозволи в **System Preferences > Security & Privacy > Privacy**:
- ✅ **Screen Recording** (для скріншотів)
- ✅ **Accessibility** (для автоматизації)

## Ігнорувати попередження

Це попередження можна ігнорувати:
```
SyntaxWarning: invalid escape sequence '\e'
```
Це внутрішнє попередження PyAutoGUI, не впливає на функціональність.

## Перевірити роботу

```bash
# Швидкий тест
./quick_test_macos.sh

# Повний тест
python3 test_screenshot_complete.py

# Тест конкретно скріншотів
python3 -c "from tools.screenshot_tool import capture_screen; img = capture_screen(); print(f'✅ {img.size}')"
```

## Готово! 🎉

Atlas готовий до роботи на macOS:
- 🖥️ GUI інтерфейс запущений
- 🤖 Gemini AI підключений  
- 📸 Screenshot інструменти працюють
- 🛠️ 24 built-in + 1 custom інструмент доступні

Використовуйте Atlas через GUI або додайте задачі через інтерфейс!
