numbers = [5, 2, 1, 7, 4]
numbers.append(20)          #adding items from back
numbers.insert(2, 10)
numbers.remove(1)       #for remove a specific item from list
numbers.pop()            # to remove last item in list
print(numbers.index(7))  # show the position on the list or existence of the item
print(50 in numbers)     #existence of the item, give True False output
print(numbers.count(5))     # count of particular item in list
numbers.sort()              # short the item on sequence wise
numbers.reverse()           # shorted in descending order
numbers2 = numbers.copy()   # number2 will not change if we do operation on numbers. because now number2 memory location change
print(numbers2)
numbers.clear()          # to removed all the items in list
print(numbers)