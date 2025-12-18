"""
Conway's Game of Life
More info at: https://en.wikipedia.org/wiki/conway%27s_Game_of_Life
Inspired by inspired by Al Sweigart's book 
'The Big Book of Small Pyton Projects': 
https://inventwithpython.com/bigbookpython/project13.html
"""


class Field:
    def __init__(self):
        pass

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
    
    You can choose size of the pattern and shown characters. Enjoy!
              """)

    def user_input(self, type: str):
        """
        User's input to set the either character of living or dead cell and size of the pattern.

        :param type: Type of user's input of type string.\n
            Aavailable values: CHAR, SIZE
        """

if __name__ == "__main__":
    new_field = Field()
    new_field.introduce()
    new_field.user_input()

