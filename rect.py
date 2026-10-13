class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width * 2 + self.height * 2
    
object = Rectangle(10, 10)
area = object.area()
perimeter = object.perimeter()

print(area)
print(perimeter)