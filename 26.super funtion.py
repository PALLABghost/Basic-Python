
class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):     #method
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):     #method ovewrighting
        print(f"It is circle with the area of  {3.14 * self.radius * self.radius}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self,color,is_filled,width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("red", is_filled = True, radius=5)      #object
square = Square("blue", is_filled= False, width= 6)     #object
triangle = Triangle("white",is_filled=True, width=5, height=8)  #object

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")
print(square.is_filled)

circle.describe()
triangle.describe()

