
def check():
    word = input("Give me your word: ")
    do_it = word[::-1]
    if do_it == word:
        print("The word is a palindrone!!")
    else:
        print("The word is not a palindrone")

stopq = input("How many times you wanna quess? ")
stop = int(stopq)

for x in range(0,stop):
    check()

