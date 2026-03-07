# Base Class: Shape with a method area() that returns 0.
# Subclass 1: Circle (needs radius). Override area() using $\pi r^2$.
# Subclass 2: Rectangle (needs length, width). Override area().
# The Test: Create a list of shapes and loop through them, calling .area() on each without checking if it's a circle or a rectangle.

class Shape : 
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self,r):
        self.radius = r
    def area(self):
        return 3.14*(self.radius**2)
class Square(Shape):
    def __init__(self,s):
        self.side = s
    def area(self):
        return self.side**2

# A list containing different types of shapes
shapes_list = [Square(4), Circle(2), Square(10), Circle(5)]

for shape in shapes_list:
    # Python doesn't care if it's a Square or Circle
    # It just calls the .area() method belonging to that specific object
    print(f"The area of this {type(shape).__name__} is: {shape.area()}")