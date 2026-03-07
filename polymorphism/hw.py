class Shape:
    """Base class for all shapes."""
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self): return self.length * self.width

class Circle(Shape):
    """Circle class inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius
    def area(self): return math.pi * (self.radius ** 2)

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area():.2f}")