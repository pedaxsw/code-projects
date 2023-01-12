import random
 

# Create a list of flashcards
flashcards = [
    {'word': 'hej', 'translation': 'hello'},
    {'word': 'tack', 'translation': 'thank you'},
    {'word': 'ja', 'translation': 'yes'},
    {'word': 'nej', 'translation': 'no'},
    {'word': 'god dag', 'translation': 'good day'}
]

# Function to select a random flashcard
def select_flashcard():
    flashcard = random.choice(flashcards)
    word = flashcard['word']
    translation = flashcard['translation']
    return (word, translation)

# Get a random flashcard and display it to the user
correct = 0
wrong = 0

def game():
    global correct
    global wrong
    word, translation = select_flashcard()
    print(word)
    answer = input("What is the translation? ")

    if answer == translation:
        print("Correct!")
        correct +=1
    else:
        print(f"Incorrect. The correct answer is {translation}.")
        wrong +=1
    print("")
for x in range(0,3):
    game()
print(f"You had {correct} answer correct and {wrong} answers wrong")
    






