from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self): return self.length * self.width

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    def area(self): return 3.14159 * (self.radius ** 2)

shapes = [Rectangle(10, 5), Circle(7)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")