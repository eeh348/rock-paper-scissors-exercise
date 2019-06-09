# game.py

import random

def my_message():
    return "HELLO"

def determine_winner(user_choice, computer_choice):
    return "PASS"


#if this script is executed from the cmd line
if __name__ == "__main__":

    print("Rock, Paper, Scissors, Shoot!")

    # CAPTURE INPUTS

    user_choice = input("Please select one of the following options: 'rock' , 'paper', or 'scissors'")

    print("-------------------")

    print("USER CHOICE", user_choice)

    # VALIDATE INPUTS

    options = ["rock", "paper", "scissors"]

    if user_choice not in options:
        print ("INVALID SELECTION. PLEASE TRY AGAIN...")
        exit()

    # GENERATE COMPUTER SELECTION

    computer_choice = random.choice(options)

    print("-------------------")
    print("GENERATING...")
    print("COMPUTER CHOICE", computer_choice)

    # DETERMINE THE WINNER

    #user_choice = "rock"
    #computer_choice = "rock"

    if user_choice == computer_choice:
        print ("Tie!", user_choice, "equals", computer_choice)
    elif user_choice == "rock":
        if computer_choice == "paper":
            print ("You lose!", computer_choice, "covers", user_choice)
        else:
            print ("You win!", user_choice, "smashes", computer_choice)
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print ("You lose!", computer_choice, "cuts",  user_choice)
        else:
            print ("You win!", user_choice, "covers", computer_choice)
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print ("You lose!", computer_choice, "smashes", user_choice)
        else: 
            print ("You win!", user_choice, "cuts",computer_choice)
        pass


print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please select one of the following options: 'rock' , 'paper', or 'scissors'")

print("-------------------")

print("USER CHOICE", user_choice)

# VALIDATE INPUTS

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print ("INVALID SELECTION. PLEASE TRY AGAIN...")
    exit()

# GENERATE COMPUTER SELECTION

computer_choice = random.choice(options)

print("-------------------")
print("GENERATING...")
print("COMPUTER CHOICE", computer_choice)

# DETERMINE THE WINNER

# rock > scissors
# scissors > paper
# paper > rock
# same selection is a tie

#user_choice = "rock"
#computer_choice = "rock"

if user_choice == computer_choice:
    print ("Tie!", user_choice, "equals", computer_choice)
elif user_choice == "rock":
    if computer_choice == "paper":
        print ("You lose!", computer_choice, "covers", user_choice)
    else:
        print ("You win!", user_choice, "smashes", computer_choice)
elif user_choice == "paper":
    if computer_choice == "scissors":
        print ("You lose!", computer_choice, "cuts",  user_choice)
    else:
        print ("You win!", user_choice, "covers", computer_choice)
elif user_choice == "scissors":
    if computer_choice == "rock":
        print ("You lose!", computer_choice, "smashes", user_choice)
    else: 
        print ("You win!", user_choice, "cuts",computer_choice)


# DISPLAY FINAL OUTPUTS / OUTCMOES