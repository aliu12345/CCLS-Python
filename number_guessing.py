# Simple Python Program: Guess the Nuumber Game

import random

def guess_the_number():
    number = random.randint(1, 10) #Generate random number between 1 and 10
    attemps = 0

    while True:
        guess = int(input("Guess a number between 1 and 10"))
        attemps += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attemps} attemps.")
            break

# Call the function to start the game
guess_the_number()