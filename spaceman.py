import random
letters_guessed = [] # list to store guessed letters
guesses_left = 0 # initializes variable
gamestate = True # initializes variable

# loads and randomizes secret_word
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

# loops though letters in secret word and checks if a letter is not in letters_guessed
def is_word_guessed(secret_word, letters_guessed):
    player_guess = ""

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            player_guess += secret_word[i]

    if secret_word == player_guess:
        return True
    else:
        return False

# loops through letters in secret words to build a string that shows letters guessed correctly and displayes an _ if the letter has not been guessed yet
def get_guessed_word(secret_word, letters_guessed):
    underscore = "_" * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            underscore = underscore[:i]  + secret_word[i] + underscore[i+1:]

    for letter in underscore:
        print(letter, end="")

# checks if the letter guess is in the secret word
def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        print("Your guess appears in the word!")
        return True
    else:
        print("Sorry, your guess was not in the word, try again")
        return False

# stores and gets rid of letters left
def alphabet_storage(guess):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if guess in alphabet:
        alphabet.remove(guess)
    else:
        pass
    print(f"\nThese letters haven't been guessed yet: {alphabet}")

# game over and game reset
def game_over(gamestate):
    letters_guessed.clear()
    play_again = input("Would you like to play again? (Y/N): ").lower()
    if play_again == 'y':
        # reset variables and play again
        print("\n\n\n\n\n\n\n\n\n\n\n")
        gamestate = True
        secret_word = load_word()
        spaceman(secret_word, 7)
        return gamestate
    else:
        print("\n\n\n\n-------------------------- Thanks for playing! --------------------------\n\n")
        return

# prompt user for input and check if there's more than one input
def prompt():
    while True:
        print("----------------------------------------------------\n")
        guessed_letter = input("Enter a letter: ").lower()
        if len(guessed_letter) > 1:
            print("\nOnly one letter is allowed! Please try again\n")
            continue
        else:
            return guessed_letter

# controls the spaceman game loop
def spaceman(secret_word, guesses_left):
    # print(secret_word) # comment this out in final version, used for testing purposes
    print(f"\nThe secret word contains: {len(secret_word)} letters\n")

    while gamestate == True:
        guess = prompt()
        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print("\nGuessed word so far: ")
            get_guessed_word(secret_word, letters_guessed)

        else:
            guesses_left -= 1
            if guesses_left <= 0:
                print(f"\n\n-------------------------- Game over! The word was {secret_word} --------------------------\n\n")
                game_over(gamestate)
                return
            else:
                pass

        if is_word_guessed(secret_word, letters_guessed):
            print("\n\n-------------------------- Congrats! You won!! --------------------------\n\n")
            game_over(gamestate)
            return

        alphabet_storage(guess)
        print(f"\nYou have {guesses_left} incorrect guesses left, please enter one letter per round\n")
        

# tutorial message/prompt
print("\n\n-------------------------- Welcome to spaceman!! --------------------------\n\n")
tutorial = input("Would you like instructions on how to play? (Y/N): ").lower()

if tutorial == "y":
    print("\n\nSpaceman is a simple game all about guessing. A random 'secret' word is selected and you are in charge of guessing what it is. You are able to guess one letter at a time but are ONLY able to have 7 incorrect guesses. Good luck!\n\n")
else:
    pass

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word, 7) #change 7 to edit how many incorrect guesses player may have