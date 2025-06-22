# Email Strategy System

## 🎯 **Огляд**

Email Strategy System автоматично вибирає найкращий спосіб доступу до email залежно від доступності та типу завдання.

## 🏗️ **Архітектура**

### **1. Gmail API (Пріоритет 1)**
- **Переваги**: Швидко, ефективно, без UI
- **Вимоги**: Автентифікація Google API
- **Використання**: Пошук, фільтрація, аналітика email

### **2. Browser Automation (Fallback)**
- **Переваги**: Працює без API, імітує користувача
- **Вимоги**: Браузер (Safari/Chrome)
- **Використання**: UI взаємодія, навігація

### **3. Hybrid Approach**
- **Логіка**: API спочатку, браузер як fallback
- **Використання**: Складні завдання з резервним планом

## 🔧 **Як це працює**

### **Автоматичний вибір методу:**

```python
# Система автоматично вибирає:
"Search for security emails" → Gmail API (якщо доступний)
"Open Safari browser" → Browser Automation
"Find emails about security" → Hybrid (API + fallback)
```

### **Логіка вибору:**

1. **Gmail API** - для пошуку, фільтрації, аналітики
2. **Browser Automation** - для UI взаємодії
3. **Hybrid** - для складних завдань з fallback

## 📋 **Налаштування**

### **Gmail API Setup:**

1. **Створіть credentials файл:**
```bash
# ~/.atlas/gmail_credentials.json
{
  "type": "service_account",
  "project_id": "your-project",
  "private_key_id": "...",
  "private_key": "...",
  "client_email": "...",
  "client_id": "..."
}
```

2. **Або використовуйте environment variables:**
```bash
export GMAIL_API_KEY="your-api-key"
export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
```

### **Browser Automation Setup:**

1. **Safari** (macOS) - працює автоматично
2. **Chrome** - потребує ChromeDriver
3. **Firefox** - потребує GeckoDriver

## 🎯 **Приклади використання**

### **Завдання для Gmail API:**
```
"Знайди всі security emails"
"Пошук листів про безпеку акаунта"
"Фільтруй email за датою"
```

### **Завдання для Browser:**
```
"Відкрий Safari і зайди в Gmail"
"Навігація по Gmail"
"Клікни на лист"
```

### **Складні завдання (Hybrid):**
```
"Знайди security emails, якщо не вийде - відкрий браузер"
"Пошук в Gmail з fallback на браузер"
```

## 🔍 **Моніторинг**

### **Логи показують:**
```
INFO: Email Strategy Manager selected gmail_api -> EmailFilter
INFO: Email Strategy Manager selected browser_automation -> BrowserTool
INFO: Gmail API failed, falling back to browser automation
```

### **Результати містять:**
```json
{
  "success": true,
  "method": "gmail_api",
  "message": "Found 5 security emails",
  "data": {...}
}
```

## 🚀 **Переваги системи**

### **1. Автоматичний вибір**
- Система сама вибирає найкращий метод
- Користувач не думає про технічні деталі

### **2. Fallback механізм**
- Якщо API не працює → браузер
- Якщо браузер не працює → повідомлення про помилку

### **3. Гнучкість**
- Підтримка різних типів завдань
- Легко додавати нові методи

### **4. Надійність**
- Множественні способи доступу
- Обробка помилок на кожному рівні

## 🔧 **Технічна реалізація**

### **Ключові компоненти:**

1. **EmailStrategyManager** - головний менеджер
2. **ToolRegistry** - інтеграція з інструментами
3. **HierarchicalPlanManager** - планування завдань

### **Потік виконання:**

```
User Request → Tool Registry → Email Strategy Manager → 
Method Selection → Tool Execution → Result
```

## 📊 **Статистика**

### **Метрики:**
- Успішність кожного методу
- Час виконання
- Частота fallback використання

### **Моніторинг:**
- Автоматичне логування
- Статистика використання
- Попередження про проблеми

## 🎯 **Майбутні покращення**

1. **Додаткові API** - Outlook, Yahoo
2. **Розширена аналітика** - статистика email
3. **Автоматична автентифікація** - OAuth flow
4. **Кешування результатів** - швидший доступ
5. **Batch обробка** - масові операції

---

**Email Strategy System** забезпечує надійний та ефективний доступ до email незалежно від доступності API або браузера. 