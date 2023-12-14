'''
Check if a value exists in a dictionary
We know how to check if the key exists in a dictionary. Sometimes it is required to check if the
given value is present.
Write a Python program to check if value 200 exists in the following dictionary.
'''
def present(sample_dict, vle):

    if vle in sample_dict.values():
        print("{} present in a dict".format(vle))
    else:
        print("{} not present in a dict".format(vle))


sample_dict = {'a': 100, 'b': 200, 'c': 300}

present(sample_dict, 200)
present(sample_dict, 23)
present(sample_dict, 100)