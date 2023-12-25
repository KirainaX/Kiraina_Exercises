import random

def guess_number():

    random_num = random.randint(1, 10)
    player_num = int(input("Enter number between 1 and 10 that u thik is the right number: "))
    if player_num > 10:
        print("The number u enter is greater than 10")
        print("guess again")
        guess_number()
    elif player_num < 1:
        print("The number u enter is less than 1")
        print("guess again")
        guess_number()
    else:
        if random_num == player_num:
            print("Well guessed!")
        else:
            guess_number()


guess_number()
print("Do you want to play again?")
again = input("enter 'y' for Yes or 'n' for No: ")
if (again.lower() == 'y') or (again == 'Y'):
    guess_number()
else:
    exit()
