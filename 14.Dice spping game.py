import random

dice_art = {
    1 : ("┌───────────┐",
         "│           │",
         "│     ●     │",
         "│           │",
         "└───────────┘"),
    2 : ("┌───────────┐",
         "│   ●       │",
         "│           │",
         "│       ●   │",
         "└───────────┘"),
    3 : ("┌───────────┐",
         "│   ●       │",
         "│     ●     │",
         "│       ●   │",
         "└───────────┘"),
    4 : ("┌───────────┐",
         "│  ●     ●  │",
         "│           │",
         "│  ●     ●  │",
         "└───────────┘"),
    5 : ("┌───────────┐",
         "│  ●     ●  │",
         "│     ●     │",
         "│  ●     ●  │",
         "└───────────┘"),
    6 : ("┌───────────┐",
         "│  ●     ●  │",
         "│  ●     ●  │",
         "│  ●     ●  │",
         "└───────────┘")
}

dice = []
total =0
number_dice = int(input("Enter the number of dice: "))

for die in range(number_dice):
    dice.append(random.randint(1, 6))

print(dice)

#for die in range(number_of_dice):
#    for line in dice_art.get(dice[die]):
 #       print(line)

for row in range(5):
    for die in dice:
        print(dice_art.get(die)[row], end="")  # print top line to buttom of every cube simultaneously . it will print first line of every cube.
    print()

for die in dice:
    total += die
print(f"Total : {total}")