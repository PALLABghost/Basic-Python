menu = {"pizza": 3.00,
        "nacho": 4.00,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00}
cart = []
total = 0

print("--------MENU----------")
for key,value in menu.items():
    print(f"{key:^10}: {value:.2f}")

while True:
    food = input("Order your item(q for quit)").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

for item in cart:
    total += menu.get(item)
    print(item, end=", ")
print()
print(f"Total: ${total}")

