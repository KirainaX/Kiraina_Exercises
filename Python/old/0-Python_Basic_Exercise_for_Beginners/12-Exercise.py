# Calculate income tax for the given income by adhering to the rules below

income = 45000
tax_to_pay = 0
print("Given income", income)

if income <= 10000:
    tax_to_pay = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_to_pay = x * 10 / 100
else:
    # first 10,000
    tax_to_pay = 0

    # next 10,000 10% tax
    tax_to_pay = 10000 * 10 / 100

    # remaining 20%tax
    tax_to_pay += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_to_pay)
