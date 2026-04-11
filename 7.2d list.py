foods = ["apple", "banana", "orange", "mango"]
vegetables =["potato", "chili", "carrot"]
meats = ["chicken", "fish", "turkey"]

groceries = [foods, vegetables , meats]
#groceries = [["apple", "banana", "orange", "mango"],
              #  ["potato", "chili", "carrot"],
              #  ["chicken", "fish", "turkey"]]
print(groceries)
print(groceries[0]) #food list
print(groceries[1][2]) # carrot

for collection in groceries:
    for food in collection:
        print(food, end= " ")
    print()

#groceries = [("apple", "banana", "orange", "mango"),
              #  ("potato", "chili", "carrot"),
              #  ("chicken", "fish", "turkey")]

#groceries = (("apple", "banana", "orange", "mango"),
              #  ("potato", "chili", "carrot"),
              #  ("chicken", "fish", "turkey"))

#groceries = ({"apple", "banana", "orange", "mango"},
              #  {"potato", "chili", "carrot"},
              #  {"chicken", "fish", "turkey"})







