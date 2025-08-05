import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f"""
          >>> Hi in Bagels game <<<
I thought a {NUM_DIGITS} digits number and you have {MAX_GUESSES} guesses to guess it.
All digits can appear only once, after each guess I'll give you a clue:
    Fermi - a correct number in the correct place
    Pico - a correct number in the incorrect place
    Bagels - no correct numbers.""")

    # OPRAVA následující 2 řádky musí být v první while smyčce, jinak se číslo při nové hře nezmění
    secret_num = get_secret_num()
    print("I have thought a number.")

    while True: # main game loop
        num_guesses = 1
        while num_guesses <= MAX_GUESSES: # SECOND
            guess = ""
            # first run: 0 != NUM_DIGIS -> True / while will 
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}")
                guess = input("> ")

            num_guesses += 1
            clues = get_clues(guess, secret_num)
            print(clues)

            if guess == secret_num:
                break # SECOND

            if num_guesses > MAX_GUESSES:
                print("You are run out of guesses.")
                print(f"The answer was: {secret_num}")
            # give a clue

        
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
        
    print("Thanks for playing.")

def get_secret_num() -> str:
    """Return a string of a NUM_DIGITS digit number"""
    numbers = [_ for _ in range(10)]
    random.shuffle(numbers)

    # OPRAVA nastavit secret_num na prázdný str() přímo, tím pádem nemusím volat metodu .join() v return a .append)
    secret_num = list()
    for i in range(NUM_DIGITS):
        secret_num.append(str(numbers[i]))

    return "".join(secret_num)

def get_clues(guess: str, secret_num: str) -> str:
    """Return a string of fermi, pico or bagels, based on comparing guess and secretNum (fermi - corect place, pico - correct number, bagels - no correct numbers)"""
    if guess == secret_num:
        return "You got it!"

    clues = list()
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")
    
    # OPRAVA v orig. je použito else - jaký je v om rozdíl
    if not len(clues):
        return "Bagels"
    
    clues.sort()
    return " ".join(clues)

if __name__ == "__main__":
    main()
