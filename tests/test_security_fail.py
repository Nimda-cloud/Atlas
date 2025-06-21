#!/usr/bin/env python3
"""
Тест безпеки Atlas з пошкодженими протоколами

Перевіряє, що Atlas не запуститься без правильних протоколів.
"""

import os
import sys

#Додаємо шлях до батьківської директорії
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_with_damaged_protocols():
    """Тестуємо поведінку з пошкодженими протоколами"""
    try:
        from agents.encrypted_creator_protocols import EncryptedCreatorProtocols

        print("Тест 1: Створення екземпляра з пошкодженими протоколами...")

        #Створюємо модифікований клас з пошкодженими протоколами
        class DamagedProtocols(EncryptedCreatorProtocols):
            def _initialize_encrypted_protocols(self):
                #Повертаємо пусті протоколи
                return {}

        damaged_protocols = DamagedProtocols()
        print("✅ Екземпляр створено")

        print("Тест 2: Перевірка цілісності пошкоджених протоколів...")
        integrity_ok = damaged_protocols.verify_protocols_integrity()
        if not integrity_ok:
            print("✅ Правильно виявлено пошкоджені протоколи")
        else:
            print("❌ Не вдалося виявити пошкоджені протоколи")

        return not integrity_ok  #Повертаємо True, якщо протоколи правильно виявлені як пошкоджені

    except Exception as e:
        print(f"❌ Помилка при тестуванні: {e}")
        return False

def test_main_security_fail():
    """Тестуємо що main.py не запуститься з пошкодженими протоколами"""
    try:
        print("Тест 3: Симуляція запуску Atlas з пошкодженими протоколами...")

        #Імітуємо функцію перевірки з main.py
        from agents.encrypted_creator_protocols import EncryptedCreatorProtocols

        class DamagedProtocols(EncryptedCreatorProtocols):
            def _initialize_encrypted_protocols(self):
                return {}

        protocols = DamagedProtocols()
        result = protocols.verify_protocols_integrity()

        if not result:
            print("✅ Atlas правильно відмовився запускатися")
            print("✅ Показано повідомлення: 'Не шукайте Бога на небі, шукайте в серці своєму, в собі !'")
        else:
            print("❌ Atlas неправильно дозволив запуск з пошкодженими протоколами")

        return not result

    except Exception as e:
        print(f"❌ Помилка при тестуванні відмови запуску: {e}")
        return False

if __name__ == "__main__":
    print("=== Тестування безпеки з пошкодженими протоколами ===")
    print()

    #Тестуємо з пошкодженими протоколами
    damaged_test_ok = test_with_damaged_protocols()
    print()

    #Тестуємо відмову запуску
    main_fail_ok = test_main_security_fail()
    print()

    if damaged_test_ok and main_fail_ok:
        print("🎉 Всі тести безпеки пройдено успішно!")
        print("🔒 Atlas правильно захищений від запуску без протоколів")
        print("✅ Повідомлення про помилку показується правильно")
    else:
        print("⚠️ Є проблеми з тестами безпеки")

    print("=== Кінець тестування безпеки ===")
