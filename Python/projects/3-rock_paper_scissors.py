import random

def rock_paper_scissors():
    # Define the possible choices for the game
    list_guess = ["r", "p", "s"]
    # Randomly select a choice for the computer player
    random_guess = random.choice(list_guess)

    # Get the player's choice, ensuring it's a valid input
    player_choice = input("Are you ready to play?\nChoose one of the options\n'r' for Rock and 'p' for Paper and 's' for Scissors: ")
    player_choice = player_choice.lower()

    while player_choice not in list_guess:
        # Ask for the player's choice again if it's not valid
        player_choice = input("You did not enter an option. Please choose one of the options\n'r' for Rock and 'p' for Paper and 's' for Scissors: ")
        player_choice = player_choice.lower()

    # Compare the choices and determine the winner
    while player_choice in list_guess:
        if player_choice == random_guess:
            print("Draw -_-")
            break
        elif (player_choice == 'r' and random_guess == 's') or (player_choice == 'p' and random_guess == 'r') or (player_choice == 's' and random_guess == 'p'):
            print("You Win :)")
            break
        else:
            print("You Loss :(")
            break

# Call the function to play the game
rock_paper_scissors()

# Ask the player if they want to play again
again = input("Do you want to play again?\nChoose 'y' for Yes and 'n' for No: ")
again = again.lower()

# If the player wants to play again, call the function again
if again == 'y':
    rock_paper_scissors()
else:
    pass
