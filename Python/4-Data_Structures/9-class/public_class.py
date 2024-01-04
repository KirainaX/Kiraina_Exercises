# Public Attributes 'WITHOUT UNDERSCORES' just '.' ex:

class Myclass:
    def __init__(self):
        self.public_attr = "This is a public attribute" # bittwen 'self' and 'attribute' just '.'

obj = Myclass()
print(obj.public_attr) # Output: This is a public attribute
