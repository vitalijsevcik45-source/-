def check_globals(func):
    def wrapper(*args, **kwargs):
        # Робимо копію глобальних змінних до запуску функції
        before = func.__globals__.copy()
        
        # Запускаємо функцію
        result = func(*args, **kwargs)
        
        # Перевіряємо змінні після запуску
        for key, value in func.__globals__.items():
            # Пропускаємо системні змінні (з подвійним підкресленням)
            if not key.startswith("__"):
                # Якщо змінна змінилась або з'явилась нова — помилка
                if key not in before or before[key] != value:
                    raise ValueError(f"Помилка: Функція змінила глобальну змінну '{key}'")
        
        return result
    return wrapper
    
