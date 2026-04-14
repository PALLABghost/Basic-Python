def show_balance(balance):
    print(f"Your Balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be Deposit: "))
    if amount < 0:
        print("That's not a valid amount ")
        return 0
    return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be Withdraw: "))
    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("Amount should be greater than zero")
        return 0
    return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("---------------------------------")
        print("        Banking program")
        print("---------------------------------")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("---------------------------------")
        choice = input("Enter your choice (1-4): ")
        print("---------------------------------")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
            show_balance(balance)
        elif choice == "3":
            balance -= withdraw(balance)
            show_balance(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")

    print("---------------------------------")
    print("   Thanks for Banking with US")
    print("---------------------------------")





if __name__ == '__main__':
    main()


