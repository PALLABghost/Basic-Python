principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter you principal amount: "))
    if principal < 0:
        print("Principal cant be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter you interest rate: "))
    if rate < 0:
        print("rate cant be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("year cant be less than or equal to zero")
    else:
        break

total = principal * pow((1 + rate / 100), time)
print(f"your Final amount {total : .2f}")