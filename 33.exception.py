#exception = try , except , finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("you cant divided by zero Idiot")
except ValueError:
    print("Enter only number please")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")
