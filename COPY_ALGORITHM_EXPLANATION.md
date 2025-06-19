# 🤖 Atlas - Алгоритм копіювання з одного вікна в інше

## 📋 Огляд процесу

Коли потрібно скопіювати щось з одного вікна в інше, Atlas виконує наступні кроки:

## 🔍 1. Виявлення та аналіз джерела

```python
# 1.1 Зробити знімок екрану для аналізу
from tools.screenshot_tool import capture_screen
screenshot = capture_screen()

# 1.2 Розпізнати текст за допомогою OCR
from tools.ocr_tool import ocr_image
text_content = ocr_image(screenshot)

# 1.3 Знайти елементи інтерфейсу
from tools.image_recognition_tool import find_object_in_image
ui_elements = find_object_in_image(screenshot, "text_field")
```

## 🎯 2. Виділення та копіювання контенту

```python
# 2.1 Перемістити мишу до початку тексту
from tools.mouse_keyboard_tool import move_mouse, click_at
move_mouse(start_x, start_y)
click_at(start_x, start_y)

# 2.2 Виділити текст (перетягування або подвійний клік)
click_at(start_x, start_y, duration=0.1)  # Встановити курсор
move_mouse(end_x, end_y, duration=0.5)    # Перетягнути для виділення

# 2.3 Скопіювати в буфер обміну
from tools.mouse_keyboard_tool import press_key
press_key("cmd+c")  # macOS
# або press_key("ctrl+c")  # Windows/Linux
```

## 📦 3. Управління буфером обміну

```python
# 3.1 Перевірити що скопійовано
from tools.clipboard_tool import get_clipboard_text
clipboard_content = get_clipboard_text()

if clipboard_content.success:
    print(f"Скопійовано: {clipboard_content.content}")
else:
    print(f"Помилка: {clipboard_content.error}")

# 3.2 Можна також програмно встановити вміст
from tools.clipboard_tool import set_clipboard_text
set_clipboard_text("Потрібний текст")
```

## 🎯 4. Знаходження цільового вікна

```python
# 4.1 Зробити новий знімок екрану
new_screenshot = capture_screen()

# 4.2 Знайти поле для вставки
target_field = find_object_in_image(new_screenshot, "input_field")

# 4.3 Або знайти конкретне вікно/додаток
# Atlas може використовувати OCR для пошуку назв вікон
app_title = find_object_in_image(new_screenshot, "window_title")
```

## 📝 5. Вставка контенту

```python
# 5.1 Активувати цільове поле
click_at(target_x, target_y)

# 5.2 Очистити поле (якщо потрібно)
press_key("cmd+a")  # Виділити все
press_key("delete") # Видалити

# 5.3 Вставити з буфера обміну
press_key("cmd+v")  # macOS
# або press_key("ctrl+v")  # Windows/Linux

# 5.4 Підтвердити вставку (якщо потрібно)
press_key("enter")
```

## 🔄 6. Повний приклад сценарію

```python
def copy_between_windows(source_coords, target_coords, selection_method="drag"):
    """
    Копіює контент з одного вікна в інше
    
    Args:
        source_coords: (x1, y1, x2, y2) координати джерела
        target_coords: (x, y) координати цілі
        selection_method: "drag", "double_click", "triple_click"
    """
    
    # Крок 1: Зробити знімок для аналізу
    screenshot = capture_screen()
    
    # Крок 2: Виділити контент у джерелі
    x1, y1, x2, y2 = source_coords
    
    if selection_method == "drag":
        # Перетягування для виділення
        click_at(x1, y1)
        move_mouse(x2, y2, duration=0.5)
        click_at(x2, y2)
    elif selection_method == "double_click":
        # Подвійний клік для виділення слова
        click_at(x1, y1)
        click_at(x1, y1, duration=0.05)
    elif selection_method == "triple_click":
        # Потрійний клік для виділення рядка
        click_at(x1, y1)
        click_at(x1, y1, duration=0.05)
        click_at(x1, y1, duration=0.05)
    
    # Крок 3: Скопіювати
    press_key("cmd+c")
    
    # Крок 4: Перевірити що скопійовано
    clipboard_result = get_clipboard_text()
    if not clipboard_result.success:
        return False, "Не вдалося скопіювати текст"
    
    # Крок 5: Перейти до цільового поля
    target_x, target_y = target_coords
    click_at(target_x, target_y)
    
    # Крок 6: Вставити
    press_key("cmd+v")
    
    return True, f"Скопійовано: {clipboard_result.content[:50]}..."
```

## 🛠️ 7. Розширені можливості

### 7.1 Копіювання зображень
```python
# Копіювання скріншоту області
region_screenshot = capture_screen_region(x1, y1, x2, y2)
set_clipboard_image(region_screenshot.tobytes())
```

### 7.2 Інтелектуальне розпізнавання контенту
```python
# OCR для автоматичного виявлення тексту
detected_text = ocr_image(screenshot)
# Знаходимо потрібний фрагмент
target_text = extract_relevant_text(detected_text, search_pattern)
```

### 7.3 Контекстна обробка
```python
# Atlas може аналізувати контекст і форматування
if is_email_field(target_coords):
    # Форматувати як email
    formatted_content = format_as_email(clipboard_content)
elif is_phone_field(target_coords):
    # Форматувати як телефон
    formatted_content = format_as_phone(clipboard_content)
```

## 🎯 8. Ключові переваги алгоритму Atlas

1. **Крос-платформеність**: Працює на macOS, Windows, Linux
2. **Інтелектуальність**: Використовує OCR та розпізнавання образів
3. **Надійність**: Множинні fallback методи для кожної операції
4. **Гнучкість**: Підтримка різних типів контенту (текст, зображення)
5. **Контекстуальність**: Аналізує тип цільового поля для правильного форматування

## 🔧 9. Технічна архітектура

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Screenshot    │───▶│       OCR       │───▶│  Recognition    │
│     Tool        │    │      Tool       │    │      Tool       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Mouse/Keyboard  │◀───│   Clipboard     │───▶│     Agent       │
│     Tool        │    │     Tool        │    │   Decision      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

Цей алгоритм дозволяє Atlas автономно виконувати складні завдання копіювання між різними додатками та вікнами з високою точністю та надійністю.
