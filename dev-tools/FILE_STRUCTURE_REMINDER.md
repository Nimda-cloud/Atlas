# Нагадування про структуру файлів Atlas

## ❗ ВАЖЛИВО: Завжди дотримуйтесь правильної структури файлів!

### Куди класти файли:

#### 🧪 Тести та тестові скрипти
- **Правильно**: `dev-tools/testing/`
- **Неправильно**: ~~корінь проекту~~

#### 📊 Звіти та аналіз
- **Правильно**: `docs/reports/`  
- **Неправильно**: ~~корінь проекту~~

#### 🔧 Інструменти розробки
- **Правильно**: `dev-tools/`
- **Підпапки**: `analysis/`, `setup/`, `documentation/`

#### 🖥️ Platform-specific код
- **Linux**: `utils/linux_utils.py` + `requirements-linux.txt`
- **macOS**: `utils/macos_utils.py` + `requirements-macos.txt`
- **Cross-platform**: `utils/platform_utils.py`

### Перевірка структури

Завжди запускайте перед commit:
```bash
python dev-tools/check_file_structure.py
```

### Швидке виправлення

Якщо файли в неправильному місці:
```bash
# Перемістити тести
mv test_*.py dev-tools/testing/

# Перемістити звіти  
mv *_REPORT.md docs/reports/
mv ANALYSIS_*.md docs/reports/

# Перемістити інструменти
mv check_*.py dev-tools/
mv fix_*.py dev-tools/
```

### Нові файли

**ПЕРЕД створенням нових файлів** - подумайте, де вони мають бути:

- 🧪 **Тест чогось** → `dev-tools/testing/`
- 📊 **Звіт/аналіз** → `docs/reports/`  
- 🔧 **Інструмент розробки** → `dev-tools/`
- 📖 **Документація** → `docs/`
- 🖥️ **Platform-specific** → `utils/`

**Ніколи не кладіть у корінь проекту файли, які можуть бути в спеціалізованих папках!**
