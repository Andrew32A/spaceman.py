import random
letters_guessed = [] # list to store guessed letters
guesses_left = 0 # initializes variable
gamestate = True # initializes variable

def load_word():
    '''
    loads and randomizes secret_word
    Returns: 
        string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word
 
def is_word_guessed(secret_word, letters_guessed):
    '''
    loops though letters in secret word and checks if a letter is not in letters_guessed
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    player_guess = ""

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            player_guess += secret_word[i]

    if secret_word == player_guess:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    loops through letters in secret words to build a string that shows letters guessed correctly and displayes an _ if the letter has not been guessed yet
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    underscore = "_" * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            underscore = underscore[:i]  + secret_word[i] + underscore[i+1:]

    for letter in underscore:
        print(letter, end="")

def is_guess_in_word(guess, secret_word):
    '''
    checks if the letter guess is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    if guess in secret_word:
        print("Your guess appears in the word!")
        return True
    else:
        print("Sorry, your guess was not in the word, try again")
        return False

def alphabet_storage(guess, alphabet):
    '''
    stores and gets rid of letters left
    Args:
        guess (string): The letter the player guessed this round
        alphabet (list): List that stores a-z
    '''
    if guess in alphabet:
        alphabet.remove(guess)
    else:
        pass
    print(f"\nThese letters haven't been guessed yet: {alphabet}")

def game_over():
    '''
    game over and game reset
    '''
    letters_guessed.clear()
    play_again = input("Would you like to play again? (Y/N): ").lower()
    if play_again == 'y':
        # reset variables and play again
        print("\n\n\n\n\n\n\n\n\n\n\n")
        secret_word = load_word()
        spaceman(secret_word, 7)
    else:
        print("\n\n\n\n-------------------------- Thanks for playing! --------------------------\n\n")
        return

def prompt():
    '''
    prompt user for input and check if input is valid
    Returns:
        guessed_letter (string): letter that user guessed
    '''
    while True:
        print("----------------------------------------------------\n")
        guessed_letter = input("Enter a letter: ").lower()
        # if guessed_letter == secret_word: # stretch goal that checks if user guessed full word; might add later
        if len(guessed_letter) > 1:
            print("\nOnly one letter is allowed! Please try again\n")
            continue
        elif guessed_letter.isalpha() == False:
            print("\nOnly letters in the alphabet are allowed! Please try again\n")
            continue
        elif guessed_letter in letters_guessed:
            print("You have already tried that letter! Please try again")
            continue
        else:
            return guessed_letter

def spaceman(secret_word, guesses_left):
    '''
    controls the spaceman game loop
    Args:
      secret_word (string): the secret word to guess.
      guesses_left (int): guesses the player has left
    '''
    # print(secret_word) # comment this out in final version, used for testing purposes
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(f"\nThe secret word contains: {len(secret_word)} letters\n")

    while gamestate == True:
        guess = prompt()
        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print("\nGuessed word so far: ")
            get_guessed_word(secret_word, letters_guessed)

        else:
            print("\nGuessed word so far: ")
            get_guessed_word(secret_word, letters_guessed)
            print("")
            guesses_left -= 1
            if guesses_left <= 0:
                print(f"\n\n-------------------------- Game over! The word was {secret_word} --------------------------\n\n")
                game_over()
                return
            else:
                pass

        if is_word_guessed(secret_word, letters_guessed):
            print("\n\n-------------------------- Congrats! You won!! --------------------------\n\n")
            game_over()
            return

        alphabet_storage(guess, alphabet)
        print(f"\nYou have {guesses_left} incorrect guesses left, please enter one letter per round\n")
        
# tutorial message/prompt
print("\n\n-------------------------- Welcome to spaceman!! --------------------------\n\n")
tutorial = input("Would you like instructions on how to play? (Y/N): ").lower()

if tutorial == "y":
    print("\n\nSpaceman is a simple game all about guessing. A random 'secret' word is selected and you are in charge of guessing what it is. You are able to guess one letter at a time but are ONLY able to have 7 incorrect guesses. Good luck!\n\n")
else:
    pass

# function calls that will start the game
secret_word = load_word()
spaceman(secret_word, 7) #change 7 to edit how many incorrect guesses player may have