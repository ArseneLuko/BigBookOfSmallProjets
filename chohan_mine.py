'''
Cho-Han game by Lukas Karásek, inspired by Al Sweigat's book 
'The Big Book of Small Pyton Projects'. My solution writen from
scratch, but I chose to use OOP concept.
'''

import random
import sys

class Game:
    pass    

class Dice:
    """Class representing a dice. If not settled, creates a six-side die."""

    japanese_numbers = {
        1: 'ICHI',
        2: 'NI',
        3: 'SAN',
        4: 'SHI',
        5: 'GO',
        6: 'ROKU',
    }

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self) -> int:
        '''Return an integer representing one side of one die.'''
        return random.randint(1, self.sides)

class Player:
    pass

if __name__ == '__main__':
    pass