# decorators.py
import functools

class GlobalVariableChangedError(Exception):
    """Виняток, що виникає при зміні глобальних змінних."""
    pass

def check_no_global_changes(func):
    """
    Декоратор, який перевіряє, чи не змінила функція глобальні змінні.
    Якщо змінні були змінені, додані або видалені — викидає помилку.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Отримуємо доступ до глобальних змінних модуля, де визначена функція
        # Використовуємо .copy(), щоб зберегти знімок стану ДО виконання
        initial_globals = func.__globals__.copy()
        
        # 2. Виконуємо функцію
        result = func(*args, **kwargs)
        
        # 3. Отримуємо актуальний стан глобальних змінних ПІСЛЯ виконання
        current_globals = func.__globals__

        # 4. Логіка перевірки
        # Перевіряємо, чи змінилися ключі (додані/видалені змінні)
        initial_keys = set(initial_globals.keys())
        current_keys = set(current_globals.keys())

        if initial_keys != current_keys:
            added = current_keys - initial_keys
            removed = initial_keys - current_keys
            error_msg = f"Global scope keys changed! Added: {added}, Removed: {removed}"
            raise GlobalVariableChangedError(error_msg)

        # Перевіряємо, чи змінилися значення існуючих змінних
        # Ігноруємо вбудовані змінні Python (починаються з __), якщо це не критично
        for key, old_val in initial_globals.items():
            if key.startswith('__'): 
                continue # Пропускаємо системні змінні
            
            new_val = current_globals[key]
            if old_val != new_val:
                raise GlobalVariableChangedError(
                    f"Global variable '{key}' was modified! Old: {old_val}, New: {new_val}"
                )

        return result
    return wrapper
  
