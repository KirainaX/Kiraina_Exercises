import random

random_number = random.randint(1, 10)
# random_number = random.random()
miss_count = 1

# print(random_number)

player_number = int(input("Enter the number you think is the correct number between 1 and 10: "))
if player_number == random_number:
    print("Well done, you guessed the number in the first time :)")
else:
    print("You guessed the wrong number :(")

while random_number != player_number:

    player_number = int(input("Enter the number you think is the correct number between 1 and 10: "))

    if player_number < 1:
        print("The number you entered is lower than 1")
    elif player_number > 10:
        print("The number you entered is greater than 10")
    elif player_number == random_number:
        if miss_count >= 3:
            miss_count = miss_count + 1
            print("Well done, you guessed the number in {} times :)".format(miss_count))
            break
        else:
            print("Well done, you guessed the number in {} time :)".format(miss_count))
            break
    else:
        print("You guessed the wrong number :(")
        miss_count = miss_count + 1
