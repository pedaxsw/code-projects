import random

randomword = random.randrange(1,101)
print(randomword)

while True:
    word = int(input("Quess your number from 1 - 100: "))
    
    if randomword == word:
        print("Correct!")
        break
    elif word < randomword:
        print("Number you are quessing is bigger.")
        continue
    else:
        print("Number you are quessing is smaller.")
        continue
print("Thanks for playing my game.")
