# game.py

import random

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

# DISPLAY FINAL OUTPUTS / OUTCMOES

