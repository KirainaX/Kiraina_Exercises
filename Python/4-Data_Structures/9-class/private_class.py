# Private Attributes 'WITH DOUBLE UNDERSCORES' just '.__' ex:
class MyClass:
    def __init__(self):
        self.__private_attr = "This is a private attributes"# bittwen 'self' and 'private_attr' just '.__'

    def get_attr(self): # hellp me to print a private attribute 
        return self.__private_attr

obj = MyClass()
#print(obj.__private_attr)  Output: AttributeError: 'MyClass' object has no attribute '__private_attr' cuz its a private
print(obj.get_attr()) # Output: This is a private attributes
