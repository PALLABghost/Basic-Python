import random
low_number = 1
high_number = 100
number = random.randint(low_number,high_number)
guesses = 0
running = True
print(f"select a number between {low_number} to {high_number}")
while running:
    user_num = input("Enter a number: ")
    if user_num.isdigit():
        user_num = int(user_num)
        guesses += 1
        if low_number>user_num>high_number:
            print("you are out of range")
            print(f"select a number between {low_number} to {high_number}")
        elif user_num > number:
            print("too high, guess again")
        elif user_num < number:
            print("too low, guess again")
        else:
            print("-----------------------------")
            print(f"CORRECT! the answer is {number}")
            print(f"number of guesses {guesses}")
            running = False
    else:
        print("Your selection isInvalid!")
        print(f"select a number between {low_number} to {high_number}")
