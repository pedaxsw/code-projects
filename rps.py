import random

options = ("Rock", "Paper", "Scissors")

pc_choice = random.randrange(0,3)
print(options[pc_choice])

quess = input("Choose from Rock, Paper, Scissors: ")

if quess.lower() == Rock and pc_choice == Scissors:
    print("You won!")
elif quess.lower() == Rock and pc_choice == Paper:
    print("PC won!")
elif quess.lower() == Rock and pc_choice == Rock:
    print("Tie!")

elif quess.lower() == Scissors and pc_choice == Scissors:
    print("Tie!")
elif quess.lower() == Scissors and pc_choice == Paper:
    print("You won!")
elif quess.lower() == Scissors and pc_choice == Rock:
    print("Pc won!")

elif quess.lower() == Paper and pc_choice == Scissors:
    print("PC won!")
elif quess.lower() == Paper and pc_choice == Paper:
    print("Tie!")
elif quess.lower() == Paper and pc_choice == Rock:
    print("You won!")

else:
    print("Please choose from Paper, Rock or Scissors...")