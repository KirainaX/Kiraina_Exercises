d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sdk = dict(sorted(d.items())) # sort by key
sdv = dict(sorted(d.items(), key=lambda item: item[1])) # sort by value

print(sdk)
print(sdv)
"""
==> OUTPUT <==
~> {0: 0, 1: 2, 2: 1, 3: 4, 4: 3} sorting by keys
~> {0: 0, 2: 1, 1: 2, 4: 3, 3: 4} sorting by values
"""
