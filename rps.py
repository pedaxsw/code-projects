import random

options = ("Rock", "Paper", "Scissors")

pc_choice = random.randrange(0,3)

quess = input("Choose from Rock, Paper, Scissors: ")

if quess == "Rock" and pc_choice == 2:
     print("You won!")
elif quess == "Rock" and pc_choice == 1:
     print("PC won!")
elif quess == "Rock" and pc_choice == 0:
    print("Tie!")
elif quess == "Scissors" and pc_choice == 2:
    print("Tie!")
elif quess == "Scissors" and pc_choice == 1:
     print("You won!")
elif quess == "Scissors" and pc_choice == 0:
    print("Pc won!")

elif quess == "Paper" and pc_choice == 2:
    print("PC won!")
elif quess == "Paper" and pc_choice == 1:
     print("Tie!")
elif quess == "Paper" and pc_choice == 0:
     print("You won!")

else:
     print("Please choose from Paper, Rock or Scissors..")

""".git\import random

options = ("rock", "paper", "scissors")

pc_choice = random.choice(options)

quess = input("Choose from Rock, Paper, Scissors: ").lower()

if quess == pc_choice:
     print("Tie!")
elif (quess == "rock" and pc_choice == "scissors") or (quess == "paper" and pc_choice == "rock") or (quess == "scissors" and pc_choice == "paper"):
     print("You won!")
else:
     print("PC won!")
"""