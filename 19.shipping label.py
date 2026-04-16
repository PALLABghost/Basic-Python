def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('pin')}")

shipping_label("Mr.", "Pallab", "Kumar", "Basak",
               street = "123 fake street",
                state = "West Bengal",
                pin = "798099")