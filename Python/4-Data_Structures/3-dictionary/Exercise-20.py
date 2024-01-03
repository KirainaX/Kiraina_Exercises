my_l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

u_value = set(val for dic in my_l for val in dic.values())

print(u_value)
"""
==> OUTPUT <==
{'S007', 'S002', 'S005', 'S009', 'S001'}
"""
