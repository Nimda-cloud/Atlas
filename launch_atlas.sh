#!/bin/bash

# Atlas macOS Quick Launch Script
# Швидкий запуск Atlas з автоматичною перевіркою

echo "🍎 Atlas macOS Quick Launch"
echo "============================"

# Перевіряємо, чи ми в правильній директорії
if [ ! -f "main.py" ]; then
    echo "❌ main.py не знайдено. Перейдіть до директорії Atlas"
    exit 1
fi

# Активуємо віртуальне середовище
if [ -d "venv-macos" ]; then
    echo "🔧 Активація venv-macos..."
    source venv-macos/bin/activate
    echo "✅ Віртуальне середовище активовано"
else
    echo "⚠️  venv-macos не знайдено, використовуємо системний Python"
fi

# Перевіряємо конфігурацію
if [ ! -f "config.ini" ]; then
    echo "📝 config.ini не знайдено, запускаємо швидке налаштування..."
    python3 setup_atlas_quick.py
fi

# Перевіряємо критичні залежності
echo "📦 Перевірка залежностей..."
python3 -c "
import sys
try:
    import google.generativeai
    import customtkinter
    print('✅ Критичні залежності встановлено')
except ImportError as e:
    print(f'❌ Відсутня залежність: {e}')
    sys.exit(1)
"

if [ $? -ne 0 ]; then
    echo "❌ Встановіть залежності: pip install -r requirements-macos.txt"
    exit 1
fi

# Перевіряємо API ключі
echo "🔑 Перевірка API ключів..."
python3 -c "
import configparser
import os

config = configparser.ConfigParser()
if os.path.exists('config.ini'):
    config.read('config.ini')
    
    # Перевіряємо Gemini ключ
    if config.has_section('Gemini') and config.has_option('Gemini', 'api_key'):
        key = config.get('Gemini', 'api_key')
        if key and not key.startswith('YOUR_'):
            print('✅ Gemini API ключ налаштовано')
        else:
            print('⚠️  Gemini API ключ потребує налаштування')
    else:
        print('❌ Gemini API ключ відсутній')
else:
    print('❌ config.ini не знайдено')
"

# Показуємо фінальний статус
echo ""
echo "🚀 Запуск Atlas..."
echo "📝 Лог буде показано нижче. Для зупинки натисніть Ctrl+C"
echo ""

# Запускаємо Atlas
python3 main.py

echo ""
echo "👋 Atlas зупинено"
