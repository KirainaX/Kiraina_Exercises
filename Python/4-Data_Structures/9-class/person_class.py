class Person:
    def __init__(self, name, age):
        self.name = name # 'name' is an attribute
        self.age = age # 'age' is an attribute

# Creating an instance of the 'Person' class
person1 = Person("Zakaria", 23)

# Accessing attributes
print(person1.name) # Output: Zakaria
print(person1.age) # Output: 23