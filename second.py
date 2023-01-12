import random

# List of Swedish words and their translations
swedish_words = {
    'hej': 'hello',
    'tack': 'thank you',
    'god morgon': 'good morning',
    'god kväll': 'good evening',
    'ja': 'yes',
    'nej': 'no'
}

while True:
    # Choose a random word from the list
    word, translation = random.choice(list(swedish_words.items()))
    
    # Ask the user to translate the word
    user_translation = input(f'Translate "{word}": ')
    
    # Check if the user's translation is correct
    if user_translation.lower() == translation:
        print('Correct!')
    else:
        print(f'Incorrect. The correct translation is "{translation}".')

