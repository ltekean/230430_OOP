import math

class Shape:
    def __init__(self):
        pass
    
    def get_area(self):
        pass
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        
    def get_area(self):
        return round((self.radius ** 2) * math.pi, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height