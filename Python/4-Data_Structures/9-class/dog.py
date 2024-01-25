class Dog():
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def rol_over(self):
        print(self.name.title() + " rolled over!")

dog1 = Dog("Sasuke", 22)

print("My dog's name is " + dog1.name.title() + ".")
print("My dog is " + str(dog1.age) + " years old.")
dog1 = Dog("myaw", 22)
dog1.sit()
dog1.rol_over()