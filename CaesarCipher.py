word = input("Give me a word you wanna cipher: ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = int(input("how many letters you wanna shift message by? "))
message = ""

for letter in word:
    index = alphabet.index(letter)
    adjust_index = index + shift
    cipher_letter = alphabet[adjust_index]
    message += cipher_letter
print(message)
