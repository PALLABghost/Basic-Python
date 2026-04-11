rows = int(input("Number of Rows: "))
columns = int(input("Number of columns: "))
symbol = input("Enter your symbol")

for x in range(rows):
    for y in range(columns):
        print(symbol, end='') #each number print on one line
    print() #new line start for complete of one loop of y