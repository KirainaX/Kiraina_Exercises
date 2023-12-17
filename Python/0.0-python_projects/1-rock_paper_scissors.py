# Rock, paper, scissors Python Project
import random

def rock_paper_scissors():
    my_list = ["Rock", "Paper", "Scissors"]
    random_choice = random.choice(my_list)

    player_choice = input("Choose one of the options Rock Paper Scissors : ")
    while player_choice not in my_list:
        print("Choose againe")
        player_choice = input("Choose one of the options Rock Paper Scissors : ")
        
    while player_choice in my_list:
        if player_choice == random_choice:
            print("Draw :|")
            break
        elif player_choice != random_choice:
            if player_choice == "Rock"  and random_choice == "Paper":
                print("You lose :(")
                break
            elif player_choice == "Paper"  and random_choice == "Scissors":
                print("You lose :(")
                break
            elif player_choice == "Scissors"  and random_choice == "Rock":
                print("You lose :(")
                break
            else:
                print("You win :)")
                break

rock_paper_scissors()
while True:
    print("Do you want to play again?")
    again = input("'y' for Yes or 'n' for No: ")
    if again == 'y':
        rock_paper_scissors()
    else:
        break
