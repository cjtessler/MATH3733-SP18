import random
from time import sleep

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

def computer_game():
    ''' Implements the alternate form of the game.'''
    print("Input the number the computer should guess: ", end='')
    target = int(input())

    # Computer guesses
    guess = 50
    low = 1
    high = 100
    while guess != target:
        guess = (low + high) // 2 
        print("The computer guess: ", guess)
        sleep(1)
        if guess < target:
            low = guess
        elif guess > target:
            high = guess
    
    # The computer guessed correctly
    print("The computer got it!")
    return False


def main():    
    print("Welcome to a guessing game!")
    print("If you would like to guess, enter 1.")
    print("If you would like the computer to guess, enter 2.")
    game_mode = int(input())
    while True:
        if game_mode == 1:
            play = game()
        else:
            play = computer_game()
        # break out of while loop if game returned False
        if not play:
            break


main()
