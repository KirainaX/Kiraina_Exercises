# Protected Attributes 'WITH A SINGLE UNDERSCORES' just '._' ex:
class MyClass:
    def __init__(self):
        self._protected_attr = "This is a protected attribute" # bittwen 'self' and 'protected_attr' just '._'

obj = MyClass()
print(obj._protected_attr) # Output: This is a protected attribute
