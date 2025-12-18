"""
Conway's Game of Life
More info at: https://en.wikipedia.org/wiki/conway%27s_Game_of_Life
Inspired by inspired by Al Sweigart's book 
'The Big Book of Small Pyton Projects': 
https://inventwithpython.com/bigbookpython/project13.html
"""

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
                self.default_value = 79
                self.question = f"Input the width of the pattern: (default: {self.default_value})"
            elif value == "HEIGHT":
                self.default_value = 30
                self.question = f"Input the height of the pattern: (default: {self.default_value})"


class Field:
    def __init__(self):
        """

        """
        self.CHAR_ALIVE = InputTypes("CHAR_ALIVE")
        self.CHAR_DEAD = InputTypes("CHAR_DEAD")
        self.WIDTH = InputTypes("WIDTH")
        self.HEIGHT = InputTypes("HEIGHT")
        self.INPUTS = (self.CHAR_ALIVE, self.CHAR_DEAD, self.WIDTH, self.HEIGHT)
        self.introduce()
        for user_input in self.INPUTS:
            self.user_input(user_input)


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

    def user_input(self, type: InputTypes) -> tuple:
        """
        User's input to get either character of living or dead cell 
        or size of the pattern. Return two characters 
        or two integers, respectively.

        :param type: Type of user's input of type string.\n
            Aavailable values: CHAR, SIZE type of built-in InputType class.\n
            Input parametr as self.CHAR or self.SIZE\n

            When self.CHAR is provide: User will be gradually prompted 
            for a character, first for representing an alive cell, 
            and then for representing a dead cell. 
            Return tuple of two strings.

            When self.SIZE is provide: User will be gradually prompted 
            for width and height. Return tuple of two integers.
        """ #TODO: aktualizovat docstring pro 4 proměnné a jednu otázku

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
    new_field = Field()

