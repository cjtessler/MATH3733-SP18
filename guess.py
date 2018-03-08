import random

def game():
    '''Implements the guessing game.'''
    # initial setup
    target = random.randrange(100)
    print("Guess a number between 1 and 100:")
    num_of_guesses = 0

    while True:
        # ask for user input
        guess = input()

        # check for valid guess
        try:
            guess = int(guess)
        except ValueError or TypeError:
            print("Please guess a integer: ")
            continue

        # increment the guess counter
        num_of_guesses += 1

        # check guess aginst target
        if guess < target:
            print('Too low. Guess again: ')
        elif guess > target:
            print('Too high. Guess again: ')
        else:
            print("That's right! It took you", num_of_guesses, "guess!")
            print("Would you like to play again? y/n")
            play_again = input()
            if play_again == "y":
                return True
            else:
                print("Thanks for playing!")
                return False

while True:
    play = game()
    # break out of while loop if game returned False
    if not play:
        break

