from checker import check_globals

# Глобальна змінна для тесту
points = 10

@check_globals
def good_func():
    # Ця функція лише читає, це ОК
    print(f"У мене {points} балів")

@check_globals
def bad_func():
    # Ця функція змінює глобальну змінну, це ПОМИЛКА
    global points
    points = 0
    print("Я все зламав")

if __name__ == "__main__":
    try:
        good_func()  # Спрацює нормально
        print("Тест 1 пройдено.")
        
        bad_func()   # Викличе помилку
    except ValueError as e:
        print(f"Тест 2 спіймав порушення: {e}")
        
