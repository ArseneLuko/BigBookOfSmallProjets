"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
This code is available at https://nostarch.com/big-book-small-python-programming
A version of this game is featured in the book, "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3 # length of the number to guess
MAX_GUESSES = 10


def main():
    print(f"""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.""")
    
    while True: # main game loop
        # secretNum stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I have thought a number.")
        print(f" You have {MAX_GUESSES} guesses to get it.")

        numGuesses = 1 # set the number of guess to first 
        while numGuesses <= MAX_GUESSES:
            guess = '' # set the guess to empty string
            # keep asking until the guess is valid
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # correct so break the out of this loop (2nd while on 35)
            if numGuesses > MAX_GUESSES:
                print("You are out of guesses.")
                print(f"The answer was: {secretNum}")

        # ask player to if they want to play again
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing.")
  

def getSecretNum() -> str:
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = [_ for _ in range(10)]
    random.shuffle(numbers)
    
    # get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess: str, secretNum: str) -> str:
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum: # first check if you got it
        return "You got it!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secretNum:
            # a correct digit is in the incorrect place
            clues.append("Pico")
    if len(clues) == 0: # alternativly: if not len(clues):
        return "Bagels"
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return " ".join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()