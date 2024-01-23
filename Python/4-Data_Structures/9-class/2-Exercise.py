"""Write a Python program to create a class and display the
namespace of that class."""

class Myclass:
    def __init__(self):
        pass

for i in Myclass.__dict__:
    print(i)