class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def bark(self):
        print('bark')

class Cat(Mammal):
    def bark(self):
        print('meow')                 # python doest like empty class so pass for pass on

dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
cat1.bark()