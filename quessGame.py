import random

word = input("type a number from 1 - 10: ")
while True:
    if word.isdigit() and int(word) < 11 and int(word) > 0:
        break
    elif not (int(word) < 11 and int(word) >0):
        word = input("Number that you have entered is not in range 1 - 10, please try again: ")
        continue
    else:
        word = input(word, " is not a number, please try again")
        continue