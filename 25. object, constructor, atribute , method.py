from car import Car

car1 = Car("Mustang", 2024, "red" ,False)
car2 = Car("Audi", 2020, "white" ,True)
print(car1.model)
print(car2.year)
print(car2.color)

car1.drive()
car1.stop()
car2.drive()

car1.describe()
car2.describe()