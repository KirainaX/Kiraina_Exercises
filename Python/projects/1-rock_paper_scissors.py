import random
def rock_paper_scissors():
    list_guess = ["r", "p", "s"]
    random_guess = random.choice(list_guess)

    player_choice = input("Are you ready to play?\nChoose one of the options\n'r' for Rock and 'p' for Paper and 's' for Scissors: ")
    player_choice = player_choice.lower()

    while player_choice not in list_guess:
        player_choice = input("You did not enter an option please choose one of the options\n'r' for Rock and 'p' for Paper and 's' for Scissors: ")
        player_choice = player_choice.lower()

    while player_choice in list_guess:
        if player_choice == random_guess:
            print("Draw -_-")
            break
        elif (player_choice == 'r' and random_guess == 's') and (player_choice == 'p' and random_guess == 'r') and (player_choice == 's' and random_guess == 'p'):
            print("You Win :)")
            break
        else:
            print("You Loss :(")
            break


rock_paper_scissors()

again = input("Do you want to play again?\nChoose 'y' for Yes and 'n' for No: ")
again = again.lower()

if again == 'y':
    rock_paper_scissors()
else:
    pass
