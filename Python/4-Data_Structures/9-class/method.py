# Method: is a function that is defined within a class in object-oriented programming(oop)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self): # Method
        return self.width * self.height

# Creating an instance
rectangle = Rectangle(10, 10000)

# Calling the method to calculate area
area = rectangle.calculate_area()
print("Area:", area) # Output: Area: 15
