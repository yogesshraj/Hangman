import string
from words import choose_word
from images import IMAGES

def is_word_guessed(secret_word, letters_guessed):
    a=True
    for i in secret_word:
        if i in letters_guessed:
            pass
        else:
            a=False
    return a

def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    going=""
    for letter in letters_left:
        if letter in letters_guessed:
            pass
        else:
            going+=letter
    return going

def hangman(secret_word):
    print secret_word
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""
    y=raw_input("Select the difficulty level[remaining lives will be adjusted accordance with your choice](easy,medium,hard): ")

    letters_guessed = []
    remaining_lives=8
    while remaining_lives>=0:

        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + available_letters
        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break

        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            print IMAGES[8-remaining_lives]
            letters_guessed.append(letter)
            print ""
            if y=="easy":
                remaining_lives-=1
                print "Your remaining lives are: ",remaining_lives
            elif y=="medium":
                remaining_lives-=2
                print "Your remaining lives are: ",remaining_lives
            elif y=="hard":
                remaining_lives-=3
                print "Your remaining lives are: ",remaining_lives
            else:
                print "Spell it correctly in difficulty input"
                break
    print "The secret word is "+secret_word
secret_word = choose_word()
hangman(secret_word)

