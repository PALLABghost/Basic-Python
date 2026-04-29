weight = input('Weight: ')
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    print(f"your weight is {int(weight) * 0.45}Kgs")
elif unit.upper() == "K":
    print(f"your weight is {int(weight) / 0.45}Kgs")