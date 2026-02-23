"""Dicemath by Lukas Karasek, inspired by: Al Sweigart's game from the book 
'The Big Book of Small Pyton Projects': 
https://inventwithpython.com/bigbookpython/project17.html

Player try to count sum of the dice in time."""

import sys
import os
from random import randint
from time import time
import subprocess

import dicemath_mine_dices as dice

class DiceRange:
    def __init__(self, min, max) -> None:
        self.min = min
        self.max = max

class Game:
    def __init__(self) -> None:
        self.game_duration = 30
        self.dice_width = 9
        self.dice_height = 5
        self.dice_range = DiceRange(2, 7)
        # self.check_terminal_size() 
        self.canvas_width, self.canvas_height = self.set_dimensions(os.get_terminal_size().columns, os.get_terminal_size().lines)
        self.canvas = {}
        self.dice_top_left_corners = []

    def run(self):
        if self.welcome_screen():
            self.change_settings()

        self.set_remaining_time()
        match = Match(self)
        pass

        # after end show results
        # do you want to play again? - all this in while Loop


    def create_dice(self):
        '''Create random number of dice in range of self.dice_num. Checks their positions if they don't overlap and return a list of tuples of their top-left corners coordinates [(x, y),].'''
        self.canvas = {}
        dice_number = randint(self.dice_range.min, self.dice_range.max)
        # dice_number = 1 # DEBUG
        dice_top_left_corners = []
        for _ in range(dice_number):
            top = randint(0, self.canvas_height - self.dice_height)
            left = randint(0, self.canvas_width - self.dice_width - 1)

            # check overlaping

            dice_top_left_corners.append((left, top))

        return dice_top_left_corners
    
    # TODO: create canvas a print canvas
    def create_canvas(self):
        for sx, sy in self.dice_top_left_corners:
            for y in range(self.dice_height):
                for x in range(self.dice_width):
                    pass # DEBUG
                    self.canvas[(sx + x, sy + y)] = dice.D1A[0][y][x]# TODO: dices

            # self.canvas[item] = 'X'


    def print_canvas(self):
        self.clear_screen()
        for y in range(self.canvas_height):
            for x in range(self.canvas_width):
                print(self.canvas.get((x, y), ' '), end='')


    def set_dimensions(self, width: int, height: int) -> tuple[int, int]:
        """Return a dimension (widht or height) if the wanted dimension is smaller than actual terminal width or height. Otherwise, method will return the actual size as a dimension.
        
        Method substract 3 lines from height for room to enter the sum. """
        if width > os.get_terminal_size().columns:
            width = os.get_terminal_size().columns

        if height > os.get_terminal_size().lines:
            height = os.get_terminal_size().lines

        height -= 3
        
        return (width, height)


    def check_terminal_size(self):
        if (os.get_terminal_size().columns < 79 or 
            os.get_terminal_size().lines < 24):
            print(f'Please run the game in bigger terminal. Minimal dimensions are 79 characters width and 24 characters heigh.')
            sys.exit()


    def welcome_screen(self):
        '''Welcome player and print initial settings. Ask player if they want to change and return True if so or False if they don't want do any changes.'''

        self.clear_screen()
        print(f'''Welcome to play \'Dicemath\' game. 
I will roll the dice and you will try to sum up their values ASAP. You have a limited time to do so.
Initial settings are: 
Game time: {self.game_duration} seconds
Number of dice: {self.dice_range.min} to {self.dice_range.max - 1} dice
              
Do you want to change these settings? type: 'y' or yes to change settings or Enter to start play''')
        
        if input('> ').lower().startswith('y'):
            return True
        
        return False


    def change_settings(self):
        '''Change game settings, time and number of dice.'''

        self.clear_screen()
        print(' == Game Settings ==')
        print('How much time you want to have to guess? Enter whole number in seconds, minimum 10, maximum 120.')

        self.game_duration = self.get_limit('time', 10, 120)

        print(f' {'-' * self.canvas_width} ')
        print('How many dice you want to play with? Enter whole numbers, first lower limit, second upper limit. (minimum 1, maximum 8)')
        
        lower = self.get_limit('lower', 1, 7)
        upper = self.get_limit('upper', lower + 1, 8)

        
        self.dice_range = DiceRange(lower, upper)


    def get_limit(self, limit_type: str, min_limit: int, max_limit: int) -> int:
        """Get limits from user and checks their mininal and maximal values."""
        while True:
            user_input = input(f'Enter {limit_type} limit > ')
            if user_input.isdecimal() and min_limit <= int(user_input) <= max_limit:
                return int(user_input)
            else:
                print(f'Enter a whole number between {min_limit} and {max_limit} as a {limit_type} limit.')


    def set_remaining_time(self):
        '''Set the remaining time.'''
        self.remaining_time = time() + self.game_duration


    def clear_screen(self):
        '''Clear the terminal'''
        if sys.platform == 'win32':
            subprocess.run('cls')
        else:
            subprocess.run('clear')


class Match:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.play_game()

    def play_game(self):
        while self.game.remaining_time > time():
            self.game.dice_top_left_corners = self.game.create_dice()
            self.game.create_canvas()
            self.game.print_canvas()
            print(f'délka canvas: {len(self.game.canvas)}')
            input()

        # create diceses
        # check if they don't overlap
        # print them on screen
        # let the player answer
        # check for answer and manage points

if __name__ == '__main__':
    new_game = Game()
    new_game.run()