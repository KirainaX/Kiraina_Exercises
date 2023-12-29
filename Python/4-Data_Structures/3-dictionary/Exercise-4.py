dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key = int(input("Enter a key: "))

if key in dic:
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")

"""
==> OUTPUT <==
~> Enter a key: 1
Key is present in the dictionary
~> Enter a key: 7
Key is not present in the dictionary
"""
