"""Dicemath by Lukas Karasek, inspired by: Al Sweigart's game from the book 
'The Big Book of Small Pyton Projects': 
https://inventwithpython.com/bigbookpython/project17.html

Player try to count sum of the dice in time."""

import sys
import os
from time import time
import subprocess

import dicemath_mine_dices as dice

class Game:
    def __init__(self) -> None:
        self.game_time = 30
        self.dice_num = range(2, 7)
        self.canvas_width, self.canvas_height = self.set_dimensions(79, 24)

    def run(self):
        if self.welcome_screen():
            self.change_settings()

        self.set_remaining_time()
        self.play_game()

        # afte end show results
        # do you want to play again? - all this in while Loop


    def play_game(self):
        while self.remaining_time > time():
            print('hraješ hru') # DEBUG

        # create diceses
        # check if they don't overlap
        # print them on screen
        # let the player answer
        # check for answer and manage points


    def set_dimensions(self, width: int, height: int) -> tuple[int, int]:
        """Return a dimension (widht or height) if the wanted dimension is smaller than actual terminal width or height. Otherwise, method will return the actual size as a dimension.
        
        Method substract 3 lines from height for room to enter the sum. """
        if width > os.get_terminal_size().columns:
            width = os.get_terminal_size().columns

        if height > os.get_terminal_size().lines:
            height = os.get_terminal_size().lines

        height -= 3
        
        return (width, height)


    def welcome_screen(self):
        '''Welcome player and print initial settings. Ask player if they want to change and return True if so or False if they don't want do any changes.'''

        self.clear_screen()
        print(f'''Welcome to play \'Dicemath\' game. 
I will roll the dice and you will try to sum up their values ASAP. You have a limited time to do so.
Initial settings are: 
Game time: {self.game_time} seconds
Number of dice: {self.dice_num.start} to {self.dice_num.stop - 1} dice
              
Do you want to change these settings? type: 'y' or yes to change settings or Enter to start play''')
        
        if input('> ').lower().startswith('y'):
            return True
        
        return False


    def change_settings(self):
        '''Change game settings, time and number of dice.'''

        self.clear_screen()
        while True:
            print('How much time you want to have to guess? Enter whole number in seconds, minimum 10, maximum 120.')
            time = input('> ')
            if time.isdecimal() and 10 <= int(time) <= 120:
                self.game_time = int(time)
                break

        print('How many dice you want to play with? Enter whole numbers, first lower limit, second upper limit. (minimum 1, maximum 8)')
        while True:
            lower = input('enter lower limit > ')
            if lower.isdecimal() and 1 <= int(lower) <= 7:
                lower = int(lower)
                break

        while True:
            upper = input('enter upper limit > ')
            if upper.isdecimal() and lower < int(upper) <= 8:
                upper = int(upper)
                break
        
        self.dice_num = range(lower, upper + 1) # add 1 to include it in range


    def set_remaining_time(self):
        self.remaining_time = time() + self.game_time


    def clear_screen(self):
        '''Clear the terminal'''
        if sys.platform == 'win32':
            subprocess.run('cls')
        else:
            subprocess.run('clear')



if __name__ == '__main__':
    new_game = Game()
    new_game.run()