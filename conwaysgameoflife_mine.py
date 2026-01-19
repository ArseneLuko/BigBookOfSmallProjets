"""
Conway's Game of Life
More info at: https://en.wikipedia.org/wiki/conway%27s_Game_of_Life
Inspired by Al Sweigart's book 'The Big Book of Small Pyton Projects': 
https://inventwithpython.com/bigbookpython/project13.html
Writen from scratch using OOP concept as an excercise.
"""

from random import randint
import sys
import os
import time

class InputTypes:
    """
    Class to represent the type of user input.

    Possible values are: 'CHAR_ALIVE', 'CHAR_DEAD', 'WIDTH', 'HEIGHT'
    """
    allow_values = ("CHAR_ALIVE", "CHAR_DEAD", "WIDTH", "HEIGHT")

    def __init__(self, value: str):
        """
        Check if the value is 'CHAR_ALIVE', 'CHAR_DEAD', 'WIDTH' 
        or 'HEIGHT' and assign the value.
        """
        if value not in self.allow_values:
            raise ValueError(f"Invalid value '{value}'. Must be either 'CHAR_ALIVE', 'CHAR_DEAD', 'WIDTH', 'HEIGHT'")
        self.value = value #TODO: je potřeba tento parametr?

        actual_width, actual_height = os.get_terminal_size()

        if value in ("CHAR_ALIVE", "CHAR_DEAD"):
            self.warning = "Please input only one character."

            if value == "CHAR_ALIVE":
                self.default_value = '#'
                self.question = f"Input character for living cell: (default: '{self.default_value}')"
            elif value == "CHAR_DEAD":    
                self.default_value = ' '
                self.question = f"Input character for dead cell: (default: '{self.default_value}')"

        elif value in ("WIDTH", "HEIGHT"):
            self.warning = ("Please enter a number between 3 and 79 (included)")

            if value == "WIDTH":
                self.default_value = actual_width
                self.question = f"Input the width of the pattern: (default: {self.default_value})"
            elif value == "HEIGHT":
                self.default_value = actual_height
                self.question = f"Input the height of the pattern: (default: {self.default_value})"

    def __repr__(self):
        return f"InputTypes({self.value})"

class Game:
    def __init__(self):
        """
        """
        self.game_atrib = {} 

        self.CHAR_ALIVE = InputTypes("CHAR_ALIVE")
        self.CHAR_DEAD = InputTypes("CHAR_DEAD")
        self.WIDTH = InputTypes("WIDTH")
        self.HEIGHT = InputTypes("HEIGHT")
        self.INPUTS = (self.CHAR_ALIVE, self.CHAR_DEAD, self.WIDTH, self.HEIGHT)

        # přesunout do Field
        self.cells_actual = {}
        self.cells_next = {}

    def run(self):
        """
        The process of life will begin.
        """
        self.get_attributes()
        self.main_loop()

    def get_attributes(self):
        for input_types in self.INPUTS:
            user_input = self.user_input(input_types)
            self.game_atrib[input_types] = user_input

    def main_loop(self):
        while True:
            try:
                time.sleep(.5)
                self.create_random_field()
                self.print_actual_field()
            except KeyboardInterrupt:
                print('Thanks for watching the life. See you next time.')
                sys.exit()

    def print_actual_field(self) -> None:
        """
        Prints characters representing live/dead cells stored 
        in self.cells_actual.
        """
        os.system('clear')
        for y in range(self.game_atrib[self.HEIGHT]):
            for x in range(self.game_atrib[self.WIDTH]):
                if self.cells_actual[(x, y)] == 1:
                    print(self.game_atrib[self.CHAR_ALIVE], end="")
                else:
                    print(self.game_atrib[self.CHAR_DEAD], end="")
            print()

    def create_random_field(self) -> None:
        """
        Create random field of alive/dead cells and store it in self.cells_next.
        1 - represent alive cell, 0 - represent dead cell
        """
        for y in range(self.game_atrib[self.HEIGHT]):
            for x in range(self.game_atrib[self.WIDTH]):
                self.cells_next[(x, y)] = randint(0, 1)
        
        self.cells_actual = self.cells_next

    def introduce(self) -> None:
        """
        Just wlelcome user and introduce itself at the top of the script =)
        """
        print("""
    Welcome in Conway\'s Game of Life
    The script will create a pattern of (non)living cells based on 3 rules:
        - Living cells with two or three neighbors stay alive in the next step of the simulation.
        - Dead cells with exactly three neighbors become alive in the next step of the simulation.
        - Any other cell dies or stays dead in the next step of the simulation
    
    You can choose size of the pattern and shown characters. 
    If you omit any answer, defalut values will be used.          
              
        Enjoy!
              """)

    def user_input(self, type: InputTypes) -> str | int:
        """
        Gets user input for either characters representing living/dead cells 
        or the size of the pattern. Returns either a string or an integer, 
        depending on the provided type.

        :param type: The type of user input, provided by the 
            built-in InputType class .\n
            Aavailable values: self.CHAR_ALIVE, self.CHAR_DEAD, self.WIDTH, self.HEIGHT\n

            When self.CHAR_ALIVE or self.CHAR_DEAD is provided: The user 
            is prompted to enter a character, first for 
            representing an alive cell, then for representing a dead cell. 
            This returns a string.

            When self.WIDTH or self.HEIGHT is provided: The user is prompted 
            to enter values for width or height of the 
            pattern. This returns an integer.
        """

        print(type.question)
        while True:
            temp_answer = input(" > ")
            if temp_answer == '':
                self.returns = type.default_value
                break
            elif type in (self.CHAR_ALIVE, self.CHAR_DEAD):
                if len(temp_answer) != 1:
                    print(type.warning)
                    continue
                else:
                    self.returns = temp_answer
                    break
            elif type in (self.WIDTH, self.HEIGHT):
                if not temp_answer.isdecimal():
                    print(type.warning)
                    continue
                elif not (3 <= int(temp_answer) <= 79):
                    print(type.warning)
                    continue
                else:
                    self.returns = int(temp_answer)
                    break
        
        return self.returns


if __name__ == "__main__":
    new_field = Game()
    new_field.run()

