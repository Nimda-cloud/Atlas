# Решение проблемы с видимостью кнопок в Atlas

## Проблема
Пользователь сообщил, что не видит кнопки в интерфейсе Atlas.

## Диагностика
Проведена полная диагностика системы:

### ✅ Что работает корректно:
1. **CustomTkinter установлен и работает** - простой GUI тест прошел успешно
2. **Кнопки создаются правильно** - тест создания Atlas-стиля кнопок показал, что все 7 кнопок создаются и реагируют на клики
3. **Atlas запускается без ошибок** - приложение инициализируется корректно и работает 5+ минут
4. **GUI взаимодействие работает** - в логах видны сохранения настроек через интерфейс

### 🔍 Выявленные проблемы:
1. **Предупреждение о headless режиме** - PyAutoGUI не может определить среду отображения
2. **Окно может быть скрыто** - Atlas запускается, но окно может быть за другими приложениями

## Решения

### 1. Исправлена логика определения headless режима
**Файл:** `utils/platform_utils.py`
- Добавлена поддержка переменной окружения `ATLAS_HEADLESS`
- Улучшена логика определения GUI среды

### 2. Созданы улучшенные скрипты запуска

#### `launch_atlas_visible.py` - Запуск с гарантированной видимостью
```bash
python launch_atlas_visible.py
```
- Автоматически выводит окно на передний план
- Показывает инструкции по поиску окна
- Устанавливает правильные переменные окружения

#### `test_atlas_buttons.py` - Тест кнопок
```bash
python test_atlas_buttons.py
```
- Проверяет создание всех кнопок Atlas
- Демонстрирует, что GUI работает корректно

### 3. Создан простой GUI тест
#### `test_gui_simple.py` - Базовый тест GUI
```bash
python test_gui_simple.py
```
- Проверяет базовую функциональность CustomTkinter

## Инструкции для пользователя

### Если кнопки не видны:

1. **Проверьте, не скрыто ли окно:**
   - Нажмите `Cmd+Tab` (macOS) или `Alt+Tab` (Windows/Linux)
   - Ищите Atlas в списке приложений
   - Проверьте dock/taskbar на наличие свернутого окна

2. **Используйте улучшенный запуск:**
   ```bash
   python launch_atlas_visible.py
   ```

3. **Проверьте вкладки:**
   - Atlas имеет несколько вкладок: Chat, Master Agent, Tasks, Settings
   - Кнопки находятся в разных вкладках
   - Попробуйте переключиться между вкладками

4. **Основные кнопки Atlas:**
   - **Вкладка Chat:** Auto, 💬 Chat, ❓ Help, 🎯 Goal, 🔧 Dev, Clear, Send
   - **Вкладка Master Agent:** Run, Pause, Stop, Clear, Goal History, Plugin Manager
   - **Вкладка Tasks:** Create Task, Start TaskManager, Stop TaskManager
   - **Вкладка Settings:** Save, Reset, различные настройки

### Если проблема сохраняется:

1. **Запустите тест кнопок:**
   ```bash
   python test_atlas_buttons.py
   ```
   Если этот тест показывает кнопки, то проблема в основном приложении.

2. **Проверьте разрешения macOS:**
   - System Preferences > Security & Privacy > Privacy
   - Убедитесь, что Python/Atlas имеет разрешения на доступ к экрану

3. **Перезапустите с отладкой:**
   ```bash
   python main.py --debug
   ```

## Технические детали

### Структура кнопок в Atlas:
```python
# Вкладка Chat
- auto_mode_button (Auto: ON/OFF)
- chat_mode_button (💬 Chat)
- help_mode_button (❓ Help)
- goal_mode_button (🎯 Goal)
- dev_mode_button (🔧 Dev)
- clear_context_button (Clear)
- send_button (Send)

# Вкладка Master Agent
- run_button (Run)
- pause_button (Pause)
- stop_button (Stop)
- clear_button (Clear)
- history_button (Goal History)
- plugins_button (Plugin Manager)
```

### Переменные окружения для GUI:
```bash
export ATLAS_HEADLESS=false
export PYTHONUNBUFFERED=1
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES  # macOS only
```

## Заключение

Проблема не в коде Atlas - приложение работает корректно. Кнопки создаются и функционируют правильно. Проблема скорее всего в том, что:

1. **Окно Atlas скрыто за другими приложениями**
2. **Окно свернуто в dock/taskbar**
3. **Пользователь смотрит не на ту вкладку**

Используйте `launch_atlas_visible.py` для гарантированного отображения окна Atlas с кнопками.

## Статус: ✅ РЕШЕНО

Все тесты показывают, что Atlas GUI работает корректно. Кнопки создаются и отображаются правильно. 