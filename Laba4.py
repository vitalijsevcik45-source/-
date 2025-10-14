def format_price(value):
    return f'ціна: {value:.2f} грн'

def available_products(**products):
    return products

def make_order(order, prices, stock):
    for item in order:
        if not stock.get(item, False):
            return "Замовлення не можливе, не вистачає певних товарів"
    total = sum(prices[item] for item in order)
    return f"Ваше замовлення прийнято. Загальна {format_price(total)}"

prices = {
    "хліб": 30,
    "сир": 35,
    "ковбаса": 40,
    "яйця": 100
}

stock = available_products(хліб=True, сир=True, ковбаса=False, яйця=True)

while True:
    print("\nМеню:")
    print("1. Переглянути ціну товарів")
    print("2. Зробити замовлення")
    print("3. Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        print("\nЦіни на товари:")
        for item, price_value in prices.items():
            print(f"{item} - {format_price(price_value)}")
    elif choice == "2":
        order_input = input("Введіть товари через кому: ")
        order_list = [item.strip() for item in order_input.split(",")]
        result = make_order(order_list, prices, stock)
        print(result)
    elif choice == "3":
        print("Дякуємо за візит!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
