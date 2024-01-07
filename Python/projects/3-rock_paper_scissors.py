# Import the 'random' module to generate random choices
import random

# Define a function for the Rock-Paper-Scissors game
def rock_paper_scissors():
    
    # List of possible choices: 'r' for Rock, 'p' for Paper, 's' for Scissors
    list_guess = ["r", "p", "s"]
    
    # Randomly select a choice for the computer opponent
    random_guess = random.choice(list_guess)

    # Get the player's choice and ensure it is valid
    player_choice = input("==> Are you ready to play?\nChoose one of the options\n'r' for Rock and 'p' for Paper and 's' for Scissors: ")
    player_choice = player_choice.lower()

    # Validate the player's input
    while player_choice not in list_guess:
        print("")
        player_choice = input("==> You did not enter an option. Please choose one of the options\n'r' for Rock and 'p' for Paper and 's' for Scissors: ")
        player_choice = player_choice.lower()

    # Compare the player's choice with the computer's choice to determine the winner
    while player_choice in list_guess:
        if player_choice == random_guess:
            print("")
            print("==> Draw -_-")
            break
        elif (player_choice == 'r' and random_guess == 's') or (player_choice == 'p' and random_guess == 'r') or (player_choice == 's' and random_guess == 'p'):
            print("")
            print("==> You Win :)")
            break
        else:
            print("")
            print("==> You Loss :(")
            break

# Call the Rock-Paper-Scissors function to play the game
rock_paper_scissors()

# List of valid responses for playing again
listyn = ['y', "yes", 'n', "no"]

# Ask the player if they want to play again
print("")
player_chose = input("==> Do you want to play again?\n'y' for Yes and 'n' for No: ")
player_chose = player_chose.lower()

# Continue asking until a valid response is given
while True:
    print("")
    if player_chose not in listyn:
        player_chose = input("==> Please enter 'y' for Yes and 'n' for No: ")
    elif player_chose in listyn[0:2]:
        # If the player wants to play again, call the Rock-Paper-Scissors function
        rock_paper_scissors()
        print("")
        player_chose = input("==> Do you want to play again?\n'y' for Yes and 'n' for No: ")
        player_chose = player_chose.lower()
    elif player_chose in listyn[2:]:
        # If the player does not want to play again, exit the loop
        break
