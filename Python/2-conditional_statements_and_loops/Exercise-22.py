year_human = int(input("Enter age of human: "))

if year_human == 2:
    print("The dog's age in dog's years is 10.5")
elif year_human > 2:
    human_age = 2 * 10.5 + ((year_human - 2) * 4)
    print("The dog's age in dog's years is {}".format(human_age))
else:
    print("didnt born yet")