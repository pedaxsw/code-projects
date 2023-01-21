import random


while True:
    word = input("type a number from 1 - 10: ")
    if word.isdigit():
        pass
        if int(word) < 11 and int(word) >0:
            break
        else:
             word = input("Number that you have entered is not in range 1 - 10, please try again: ")
             if word is not word.isdigit():
                break

    else:
        word = input(word, " is not a number, please try again")






