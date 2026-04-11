foods = []
prices = []
total =  0

while True:
    food = input("Enter food name(q for quit): ")
    if food.lower() == 'q':
        break
    else:
        price = int(input("Enter the price of the food: "))
        foods.append(food)
        prices.append(price)
print("-----------CART----------------")
for x in foods:
    print(x,end=" ")
for y in prices:
    total += y
print()
print(f"Your total price is {total}")
