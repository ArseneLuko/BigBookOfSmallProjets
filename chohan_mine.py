'''
Cho-Han game by Lukas Karásek, inspired by Al Sweigart's book 
'The Big Book of Small Pyton Projects'. My solution writen from
scratch, but I chose to use OOP concept.
'''

import random
import sys
from chohan_language import messages_en as messages

class Game:    
    def __init__(self):
        """
        Create a game with a player, dealer.
        """
        self.games_count = 1
        self.print_message()
        self.print_message(messages["welcome"])
        self.print_message()
        # self.player = Player('Janek', 4000) # testing line
        self.player = Player(*self.get_new_game_values())
        self.dealer = Dealer()
        self.main_game_loop()

    def main_game_loop(self):
        self.print_message(messages["bet_and_purse"].format(self.player.purse.get_value()))
        self.bet = self.get_bet()

    def get_new_game_values(self):
        self.print_message(messages["enter_name"])
        self.name = input("| ")
        self.print_message(messages["enter_money"])

        while True:
            self.money_value = input("| ")
            if self.money_value == '':
                self.money_value = 5_000
                break
            elif not self.money_value.isdecimal():
                self.print_message(messages["not_decimal"])
            else:
                self.money_value = int(self.money_value)
                break

        return (self.name, self.money_value)
    
    def print_message(self, message: str = messages["separator"]):
        """
        Prints the input after the '| ' string at the beginning. Total length of a string is 80 characters.

        :param message: A string to print from imported languege file. If not set, initial value is 'separator' string of 78 times '-'
        """
        print(f"| {message: <78}")

    def get_bet(self):
        """
        Get bet from user and control if it is a number and if the player have enough to bet.
        """
        while True:
            self.bet = input("| ")
            if not self.bet.isdecimal():
                self.print_message(messages["not_a_number"])
            elif int(self.bet) > self.player.purse.get_value():
                self.print_message(messages["not_enough"].format(self.player.purse.get_value()))
            else:
                self.bet = int(self.bet)
                self.print_message(messages["bet_accepted"].format(self.bet))
                break
        return self.bet

    
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
        self.roll_number = 1 
        self.rolls_history = {}

    def roll_die(self) -> int:
        '''Return an integer representing a roll of the die.'''

        self.roll = random.randint(1, self.sides)
        self.rolls_history[self.roll_number] = self.roll
        self.roll_number += 1
        return self.roll
    
    def get_rolls_history(self):
        return self.rolls_history


class Dealer(Game):
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

    
    def roll_dice(self):
        """
        Roll all dealer's dice
        """
        for i in range(self.number_of_dice):
            self.hod = self.dice[i + 1].roll_die()
            super().print_message(f'{i + 1}. kostkou jsem hodil {self.hod}')


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