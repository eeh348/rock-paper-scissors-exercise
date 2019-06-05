# game.py

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please select one of the following options: 'rock' , 'paper', or 'scissors'")

print("-------------------")

print("USER CHOICE", user_choice)

# VALIDATE INPUTS

if user_choice in ["rock", "paper", "scissors"]:
    print ("VALID")
else:
    print ("INVALID SELECTION. PLEASE TRY AGAIN...")
    exit()

# GENERATE COMPUTER SELECTION

print("GENERATING...")

# DETERMINE THE WINNER

# DISPLAY FINAL OUTPUTS / OUTCMOES

