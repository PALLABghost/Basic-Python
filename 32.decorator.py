#a function that extent another function without modifying the base function

def add_sprinkles(func):
    def wrapper(*args,**kwargs):        #innter function is created because without it when we if we
                                        # didnt call the get_icecream function also it will execute
        print("you added sprinkles ♨️")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("you added fudge 🍫")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_icecream(flavour):
    print(f"Here is your {flavour} icecream 🍦")

get_icecream("vanilla")