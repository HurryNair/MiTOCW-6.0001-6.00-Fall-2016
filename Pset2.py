# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    state = True
    for s in secret_word:
        if s not in letters_guessed:
            state = False
    return state


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    dynamic_guess = ""
    for c in secret_word:
        if c in letters_guessed:
            dynamic_guess = dynamic_guess + c
        else:
            dynamic_guess = dynamic_guess + "_ "
    return dynamic_guess



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lowercase = string.ascii_lowercase
    for c in lowercase:
        if c in letters_guessed:
            lowercase = lowercase.replace(c, '')
    return lowercase

def guess_checker(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: Boolean, True if all characters in secret_word are present in letters_guessed
    False otherwise
    '''
    Guessed = True
    for c in secret_word:
        if c in letters_guessed:
            continue
        elif c not in letters_guessed:
            Guessed = False
    return Guessed


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''


    print("Welcome to the game Hangman! \nI am thinking of a word that is " + str(len(secret_word)) + "letters long.\n-------------")
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []

    while guesses_remaining > 0:
        print("You have " + str(warnings_remaining) + " warnings left.")
        print("You have " + str(guesses_remaining) + " guesses left.")
        print("Available letters: " + get_available_letters((letters_guessed)))
        guess = input("Please guess a letter: ").lower()

        #User inputs his guess here

        #First the input is tested to see whether or whether not it is a
        #valid alphabet

        if guess.isalpha() != True:
            if warnings_remaining > 0:
                warnings_remaining = warnings_remaining - 1
                print(" Oops! That is not a valid letter. You have" + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
                print("------------")
                continue
            else:
                guesses_remaining = guesses_remaining - 1
                print(" Oops! That is not a valid letter. You have" + str(guesses_remaining) + " guesses left: " + get_guessed_word(secret_word, letters_guessed))
                print("------------")
                continue
        elif guess.isalpha() == True:

            #If the input is an alphabet
            #then we check if the user is repeating guesses

            if guess in letters_guessed:
                if warnings_remaining > 0:
                    warnings_remaining = warnings_remaining - 1
                    print(" Oops! You've already guessed that letter. You now have " + str(warnings_remaining) + " warnings: " + get_guessed_word(secret_word, letters_guessed) )
                    print("------------")
                    continue
                else:
                    guesses_remaining = guesses_remaining - 1
                    print(" Oops! You've already guessed that letter. You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
                    print("------------")
                    continue
            elif guess not in letters_guessed:

                #if the user has guessed a unique alphabet
                #we go ahead and append that to our list of guesses

                letters_guessed.append(guess)

                Guess = guess_checker(secret_word, letters_guessed)

                if Guess == True:
                    break

                if guess in secret_word:
                    print("Good guess: ", get_guessed_word(secret_word, letters_guessed))

                if guess not in secret_word:
                    vowels = ["a", "e", "i", "o", "u"]
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                    if guess in vowels:
                        guesses_remaining = guesses_remaining - 2
                    elif guess not in vowels:
                        guesses_remaining = guesses_remaining -1



        print("------------")


    if guesses_remaining == 0:
        print("Sorry, you ran out of guesses. The word was " + secret_word)

    elif guesses_remaining > 0:
        print("Congratulations, you won! Your total score for this game is: " + str(guesses_remaining * len(secret_word)))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''

    my_word = my_word.replace(" ", "")
    pattern_flag = 0
    for i in range(0,len(my_word)):
        if len(other_word) != len(my_word):
            return False
        elif len(my_word) == len(other_word):
            if my_word[i] == "_":
                pattern_flag += 1
                continue
            elif my_word[i] == other_word[i]:
                pattern_flag += 1
    if pattern_flag == len(my_word):
            return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    wordlist = load_words()
    match_flag = False
    for word in wordlist:
        Match = match_with_gaps(my_word, word)
        if Match == True:
            match_flag = True
            print(word)
    if match_flag == False:
        print("No matches found.")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman! \nI am thinking of a word that is " + str(
        len(secret_word)) + "letters long.\n-------------")
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []

    while guesses_remaining > 0:
        print("You have " + str(warnings_remaining) + " warnings left.")
        print("You have " + str(guesses_remaining) + " guesses left.")
        print("Available letters: " + get_available_letters((letters_guessed)))
        guess = input("Please guess a letter: ").lower()

        # User inputs his guess here

        # First the input is tested to see whether or whether not it is a
        # valid alphabet

        if guess.isalpha() != True:
            if guess == "*":
                my_word = get_guessed_word(secret_word, letters_guessed)
                show_possible_matches(my_word)
            else:
                if warnings_remaining > 0:
                    warnings_remaining = warnings_remaining - 1
                    print(" Oops! That is not a valid letter. You have" + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
                    print("------------")
                    continue
                else:
                    guesses_remaining = guesses_remaining - 1
                    print(" Oops! That is not a valid letter. You have" + str(guesses_remaining) + " guesses left: " + get_guessed_word(secret_word, letters_guessed))
                    print("------------")
                    continue

        elif guess.isalpha() == True:

            # If the input is an alphabet
            # then we check if the user is repeating guesses

            if guess in letters_guessed:
                if warnings_remaining > 0:
                    warnings_remaining = warnings_remaining - 1
                    print(" Oops! You've already guessed that letter. You now have " + str(
                        warnings_remaining) + " warnings: " + get_guessed_word(secret_word, letters_guessed))
                    print("------------")
                    continue
                else:
                    guesses_remaining = guesses_remaining - 1
                    print(
                        " Oops! You've already guessed that letter. You have no warnings left so you lose one guess: " + get_guessed_word(secret_word, letters_guessed))
                    print("------------")
                    continue
            elif guess not in letters_guessed:

                # if the user has guessed a unique alphabet
                # we go ahead and append that to our list of guesses

                letters_guessed.append(guess)

                Guess = guess_checker(secret_word, letters_guessed)

                if Guess == True:
                    break

                if guess in secret_word:
                    print("Good guess: ", get_guessed_word(secret_word, letters_guessed))

                if guess not in secret_word:
                    vowels = ["a", "e", "i", "o", "u"]
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                    if guess in vowels:
                        guesses_remaining = guesses_remaining - 2
                    elif guess not in vowels:
                        guesses_remaining = guesses_remaining - 1

        print("------------")

    if guesses_remaining == 0:
        print("Sorry, you ran out of guesses. The word was " + secret_word)

    elif guesses_remaining > 0:
        print(
            "Congratulations, you won! Your total score for this game is: " + str(guesses_remaining * len(secret_word)))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
