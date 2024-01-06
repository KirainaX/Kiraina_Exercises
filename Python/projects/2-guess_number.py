import random

# Function to play a guessing game where the user has to guess a random number between 1 and 10.
def guess_number_game():
    # Generate a random number between 1 and 10.
    random_number = random.randint(1, 10)
    
    # Get the player's initial guess.
    player_guess = input("Enter a number between 1 and 10: ")

    # Loop until the player's guess is correct or valid.
    while player_guess:
        # Check if the input is a digit.
        if player_guess.isdigit():
            player_guess = int(player_guess)
        else:
            print("")
            # Prompt the user to enter a valid number if the input is not a digit.
            player_guess = input("You didn't enter a number between 1 and 10: ")

        # Check if the entered number is within the valid range.
        if 10 < int(player_guess):
            print("")
            player_guess = input("You didn't enter a number between 1 and 10: ")
        elif 1 > int(player_guess):
            print("")
            player_guess = input("You didn't enter a number between 1 and 10: ")
        elif player_guess == random_number:
            # If the guess is correct, congratulate the player and exit the loop.
            print("")
            print("Well done, you guessed the correct number :)")
            break
        else:
            # If the guess is incorrect, provide feedback and exit the loop.
            print("")
            print("You did not guess the correct number :(")
            print("The random number is {}\nThe number you entered is {}".format(random_number, player_guess))
            break

# Start the game by calling the function.
start = guess_number_game()

# List of acceptable responses for playing the game again.
listyn = ['y', "yes", 'n', "no"]

print("")
# Ask the player if they want to play again.
player_chose = input("Do you want to guess again?\n'y' for Yes and 'n' for No: ")
player_chose = player_chose.lower()

# Continue prompting the user until a valid response is received.
while True:
    print("")
    if player_chose not in listyn:
        # Prompt the user for a valid response if the input is not in the list.
        player_chose = input("please enter 'y' for Yes and 'n' for No: ")
    elif player_chose in listyn[0:2]:
        # If the player wants to play again, call the guess_number_game() function.
        guess_number_game()
        break
    elif player_chose in listyn[2:]:
        # If the player does not want to play again, exit the loop.
        break
