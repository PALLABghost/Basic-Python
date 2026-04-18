# used to define a method of a property of attribute
#add additional logic when read, write and delete attribute.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height =height

    @property
    def width(self):
       return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rectangle1 = Rectangle(3,4)
print(rectangle1.width)
print(rectangle1.height)

rectangle1.width = 0
rectangle1.height = 6
print(rectangle1.width)
print(rectangle1.height)

del rectangle1.width


