# main.py
from decorators import check_no_global_changes, GlobalVariableChangedError

# Глобальна змінна для тесту
COUNTER = 10

@check_no_global_changes
def clean_function(x, y):
    """Ця функція безпечна, вона працює тільки з локальними даними."""
    print(f"Running clean function: {x} + {y}")
    return x + y

@check_no_global_changes
def dirty_function():
    """Ця функція змінює глобальну змінну, тому декоратор має викинути помилку."""
    global COUNTER
    print("Running dirty function...")
    COUNTER += 5 # ЗМІНА ГЛОБАЛЬНОЇ ЗМІННОЇ
    return COUNTER

@check_no_global_changes
def adding_global_function():
    """Ця функція додає нову глобальну змінну."""
    global NEW_VAR
    print("Running adding global function...")
    globals()['NEW_VAR'] = "I am new"

if __name__ == "__main__":
    print("--- ТЕСТ 1: Безпечна функція ---")
    try:
        res = clean_function(5, 3)
        print(f"Результат: {res} (Успіх)\n")
    except GlobalVariableChangedError as e:
        print(f"ПОМИЛКА: {e}\n")

    print("--- ТЕСТ 2: Функція, що змінює глобальну змінну ---")
    try:
        dirty_function()
        print("Функція виконалася (Це погано, декоратор не спрацював)\n")
    except GlobalVariableChangedError as e:
        print(f"УСПІШНО ВІДЛОВЛЕНО ПОМИЛКУ: {e}\n")

    print("--- ТЕСТ 3: Функція, що створює нову глобальну змінну ---")
    try:
        adding_global_function()
    except GlobalVariableChangedError as e:
        print(f"УСПІШНО ВІДЛОВЛЕНО ПОМИЛКУ: {e}\n")
      
