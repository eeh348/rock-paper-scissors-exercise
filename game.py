# game.py

import random
#user_choice = str

def my_message():
    return "HELLO"

def determine_winner(u, c):
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }
    winning_choice = winners[u][c]
    return winning_choice #"rock"

# only if this script is executed from the command-line
if __name__ == "__main__":

    print("Rock, Paper, Scissors, Shoot!") # this is also a comment

    # CAPTURE INPUTS

    user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

    print("--------------")
    print("USER CHOICE:", user_choice)

    # VALIDATE INPUTS

    options = ["rock", "paper", "scissors"]

    if user_choice not in options:
        print("INVALID SELECTION, PLEASE TRY AGAIN...")
        exit()

    # GENERATE COMPUTER SELECTION

    computer_choice = random.choice(options)

    print("--------------")
    print("GENERATING...")
    print("COMPUTER CHOICE:", computer_choice)

    # DETERMINE THE WINNER
    #
    # rock beats scissors
    # paper beats rock
    # scissors beats paper
    # same selections is a tie
    #
    # first attribute represents the user, second represents the computer

    winning_choice = determine_winner(user_choice, computer_choice)

    # DISPLAY FINAL OUTPUTS / OUTCOMES

    if winning_choice:
        if winning_choice == user_choice:
            print("YOU WON")
        elif winning_choice == computer_choice:
            print("YOU LOST")
    else:
        print("TIE")

    print("Thanks for playing. Please play again!")

#if user_choice == computer_choice:
#    print ("Tie!", user_choice, "equals", computer_choice)
#elif user_choice == "rock":
#    if computer_choice == "paper":
#        print ("You lose!", computer_choice, "covers", user_choice)
#    else:
#        print ("You win!", user_choice, "smashes", computer_choice)
#elif user_choice == "paper":
#    if computer_choice == "scissors":
#        print ("You lose!", computer_choice, "cuts",  user_choice)
#    else:
#        print ("You win!", user_choice, "covers", computer_choice)
#elif user_choice == "scissors":
#    if computer_choice == "rock":
#        print ("You lose!", computer_choice, "smashes", user_choice)
#    else: 
#        print ("You win!", user_choice, "cuts",computer_choice)