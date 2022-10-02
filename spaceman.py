import random
letters_guessed = [] # list to store guessed letters
guesses_left = 7
gamestate = True

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

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
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
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
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    underscore = "_" * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            underscore = underscore[:i]  + secret_word[i] + underscore[i+1:]

    for letter in underscore:
        print(letter, end="")

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        print("Your guess appears in the word!")
        return True
    else:
        print("Sorry, your guess was not in the word, try again")
        return False

def game_over(gamestate):
    letters_guessed.clear()
    play_again = input("Would you like to play again? (Y/N) ").lower()
    if play_again == 'y':
        # reset variables and play again
        gamestate = True
        secret_word = load_word()
        spaceman(secret_word, 7)
        return gamestate
    else:
        print("Thanks for playing!")
        return

def prompt():
    while True:
        guessed_letter = input("Enter a letter: ").lower()
        if len(guessed_letter) > 1:
            print("Only one letter is allowed! Please try again")
            continue
        else:
            return guessed_letter

def spaceman(secret_word, guesses_left):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost

    print("Welcome to spaceman!!")
    tutorial = input("Would you like instructions on how to play? (Y/N) ").lower()

    if tutorial == "y":
        print("Spaceman is a simple game all about guessing. A random 'secret' word is selected and you are in charge of guessing what it is. You are able to guess one letter at a time but are ONLY able to have 7 incorrect guesses. Good luck!!")
    else:
        pass

    print(f"The secret word contains: {len(secret_word)} letters")

    while gamestate == True:
        # is_word_guessed(secret_word, letters_guessed)
        # if is_word_guessed(secret_word, letters_guessed) == True:
        #     # winning message
        #     game_over()
        # else:
        #     pass
        guess = prompt()
        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print(f"Guessed word so far: {get_guessed_word(secret_word, letters_guessed)}")
            # print(f"These letters haven't been guessed yet...")
        else:
            guesses_left -= 1
            if guesses_left == 0:
                # losing message
                game_over(gamestate)
                return
            else:
                pass

        print(f"You have {guesses_left} incorrect guesses left, please enter one letter per round")
        # print(f"These letters haven’t been guessed yet: "abcd...etc")
        get_guessed_word(secret_word, letters_guessed)




#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word, 7) #change 7 to edit how many incorrect guesses player may have