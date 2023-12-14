'''
Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting the mentioned keys from the
below dictionary.
'''

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

newDict = dict()

for k in keys:
    newDict.update({k: sample_dict[k]})

# newDict = {k: sample_dict[k] for k in keys}

print(newDict)
