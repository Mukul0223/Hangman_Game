from words import words
import random
import string

def valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = valid_word(words)
    print(word)
    word_letters = set(word) # letters in word
    alphabet  = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Displaying current guessed letters
        print("You have",lives,"lives left and Guessed letters:", ' '.join(used_letters))

        # Displaying the current state of the word with underscores
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word.")
       
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print('Invalid character. Please try again.')

    # Game is over
    if len(word_letters) == 0:
        print("Congratulations! You guessed the word correctly.")
    else:
        print("Sorry, you lost. The word was", word)

hangman()
