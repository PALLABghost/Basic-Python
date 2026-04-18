from car import Car

#class Car:
 #   def __init__(self, model, year, color, for_sale):   #__init__(self) is a constractor
 #      self.model = model
 #      self.year = year
 #      self.color = color
  #     self.for_sale =for_sale

   # def drive(self):           #mathod creation
   #     print(f"You drive the {self.color} {self.model}")

  #  def stop(self):        #mathod  creation
  #      print(f"You stop the  {self.color} {self.model}")

  #  def describe(self):
  #      print(f"{self.model} {self.color} {self.year}")}

car1 = Car("Mustang", 2024, "red" ,False)       #object created in class
car2 = Car("Audi", 2020, "white" ,True)
print(car1.model)
print(car2.year)
print(car2.color)

car1.drive()        #mathod
car1.stop()         #mathod
car2.drive()

car1.describe()
car2.describe()