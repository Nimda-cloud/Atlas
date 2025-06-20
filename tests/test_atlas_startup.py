#!/usr/bin/env python3
"""
Мінімальний тест запуску Atlas з системою безпеки

Перевіряє, що Atlas може запускатися з правильними протоколами.
"""

import sys
import os

#Додаємо шлях до батьківської директорії
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_atlas_startup():
    """Тестуємо запуск Atlas через імпорт main модуля"""
    try:
        print("Тест: Імпорт модулів Atlas...")
        
        #Імпортуємо необхідні модули
        from agents.encrypted_creator_protocols import EncryptedCreatorProtocols
        print("✅ Модуль протоколів імпортовано")
        
        #Перевіряємо протоколи
        protocols = EncryptedCreatorProtocols()
        if protocols.verify_protocols_integrity():
            print("✅ Протоколи безпеки пройдено")
        else:
            print("❌ Протоколи безпеки не пройдено")
            return False
        
        #Імпортуємо клас AtlasApp (без creation GUI)
        import main
        print("✅ Модуль main.py імпортовано успішно")
        
        #Перевіряємо, що клас AtlasApp існує
        if hasattr(main, 'AtlasApp'):
            print("✅ Клас AtlasApp знайдено")
        else:
            print("❌ Клас AtlasApp не знайдено")
            return False
        
        print("✅ Atlas готовий до запуску з системою безпеки")
        return True
        
    except Exception as e:
        print(f"❌ Помилка при тестуванні запуску: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=== Тестування запуску Atlas з системою безпеки ===")
    print()
    
    if test_atlas_startup():
        print()
        print("🎉 Тест запуску пройдено успішно!")
        print("🔒 Atlas має працювати з системою безпеки")
        print("⚠️  Примітка: GUI не запускається в тестовому режимі")
    else:
        print()
        print("❌ Тест запуску не пройдено")
        print("⚠️  Atlas може мати проблеми з запуском")
        
    print("=== Кінець тестування запуску ===")
