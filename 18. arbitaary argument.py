# *args = allows you to pass multiple non-key argument
# **kwargs = allows you to pass multiple keyword argument

def add(*args):         # WE CAN USE *num
    total =0
    for arg in args:
        total += arg
    return total

def display_name(*names):
    for name in names:
        print(name, end=" ")

print(add(1,2,3,5,6,7,9))
display_name("Pallab","kumar","basak")
print()

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_address(street = "123 fake stree",
              city = "amtala",
              state = "west bengal",
              pin = "54362")