'''
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

circle = Circle(5)
print(circle.radius)
circle.radius = 10
print(circle.radius)
'''
'''
class MyClass:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

obj = MyClass()
print(obj.public)
print(obj._protected)
print(obj.__private)  # This will raise an AttributeError
'''
