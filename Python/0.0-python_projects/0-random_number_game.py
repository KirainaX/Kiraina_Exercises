#
import random

random_number = random.randint(1, 10)

player_number = int(input("Enter the number you think is the correct number between 1 and 10: "))

if player_number < 1:
    print("The number you entered is lower than 1")
elif player_number > 10:
    print("The number you entered is greater than 10")
elif player_number == random_number:
    print("Well done, you know the number :)")
else:
    print("Your answer is wrong :(")
    print("Answer is", random_number )
