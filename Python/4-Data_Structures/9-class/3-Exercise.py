"""Write a Python program to create an instance of a
specified class and display the namespace of the said instance."""

class Car:
    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value

car1 = Car("Kiraina", "Black", 100)
'''car1 = Car()
car1.name = "Kiraina"
car1.color = "Black"
car1.value = 100'''

print(car1.__dict__)