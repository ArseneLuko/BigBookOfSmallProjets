'''
Cho-Han game by Lukas Karásek, inspired by Al Sweigart's book 
'The Big Book of Small Pyton Projects'. My solution writen from
scratch, but I chose to use OOP concept.
'''

import random
import sys

class Game:    
    def __init__(self):
        """
        Create a game with player        
        """
        self.player = Player(*self.get_new_game_values())

    def get_new_game_values(self):
        # return
        return ('Lukas', 7000) # testing line

class Purse:
    """Class representing a purse, keeps the current value of money in the purse. And have methods to update value of money in the purse."""

    def __init__(self, initial_purse):
        self.value = initial_purse

    def get_value(self) -> int:
        """Return actual value of the purse"""
        return self.value
    
class Dice:
    """Class representing a dice. If not settled, creates a six-side die."""

    #TODO: uložení hodu, přečti poslední hod

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
        '''Return an integer representing a roll of the die.'''
        return random.randint(1, self.sides)

class Dealer:
    """Class representing a dealer, they have two dice"""

    def __init__(self, number_of_dice: int=2):
        """
        Initialize a dealer.

        :param number_of_dice: Initial amount of dice. If not set, value is 2.
        """
        self.number_of_dice = number_of_dice
        self.dice = {}
        for number in range(number_of_dice):
            self.dice[number + 1] = Dice()

class Player:
    """Class representing a player, they have name and a purse."""

    def __init__(self, name: str, initial_purse: int=5_000):
        """
        Initialize a new player.

        :param name: Name of the player of type str.
        :param initial_purse: Initial amount of money in a player's purse of type int. If not set, value is 5_000.
        """
        self.name = name
        self.purse = Purse(initial_purse) # 

if __name__ == '__main__':
    newGame = Game()
    pass
