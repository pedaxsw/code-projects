import random

word = int(input("type a number from 1 - 10: "))
while True:
    if word < 11 and word > 0:
        break
    elif not word < 11 and word > 0:
        word = int(input("Number that you have entered is not in range 1 - 10, please try again: "))
        continue
    else:
           continue

randomword = random.randrange(1,101)
print(randomword)

while True:
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