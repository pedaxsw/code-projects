import random

word = int(input("type a number from 1 - 10: "))
while True:
    if word < 11 and word > 0:
        break
    elif not word < 11 and word > 0:
        word = int(input("Number that you have entered is not in range 1 - 10, please try again: "))
        continue
    else:
           break