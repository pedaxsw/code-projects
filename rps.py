import random

options = ("Rock", "Paper", "Scissors")

pc_choice = random.randrange(0,3)
print(options[pc_choice])

quess = input("Choose from Rock, Paper, Scissors: ")

if quess.lower() == Rock:

