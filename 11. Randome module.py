import random
low =1
high = 10
option = ("rock", "paper", "scissor")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]

print(random.randint(1,10))
print(random.randint(low,high))
print(random.random())

print(random.choice(option))

random.shuffle(cards)
print(cards)
