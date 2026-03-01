"""Dicemath by Lukas Karasek, inspired by: Al Sweigart's game from the book 
'The Big Book of Small Pyton Projects': 
https://inventwithpython.com/bigbookpython/project17.html

Player try to count sum of the dice in time."""

import sys
import os
import random
import subprocess
from time import time

import dicemath_mine_dices as dice


class DiceNumber:
    def __init__(self, min, max) -> None:
        self.min = min
        self.max = max
        # self.min, self.max = 30, 30 # DEBUG


class GameSettings:
    def __init__(self) -> None:
        self.check_terminal_size()
        self.game_duration = 30
        # self.game_duration = 300 # DEBUG
        self.dice_width = 9
        self.dice_height = 5
        self.dice_number = DiceNumber(2, 7)
        self.canvas_width, self.canvas_height = self.set_dimensions(os.get_terminal_size().columns, os.get_terminal_size().lines)
        self.canvas = {}
        self.dice = []
        self.dice_top_left_corners = []


    def run(self):
        if self.welcome_screen():
            self.change_settings()

        self.set_remaining_time()
        match = Match(self)

        # after end show results
        # do you want to play again? - all this in while Loop


    def distribute_dice(self, dice_number):
        '''Create random coordinates for dice in self.dice. Checks their positions if they don't overlap and return a list of tuples of their top-left corners coordinates [(x, y),].'''

        # dice_number = 1 # DEBUG
        dice_top_left_corners = []
        for _ in range(dice_number):

            while True:
                left = random.randint(0, self.canvas_width - 1 - self.dice_width)
                top = random.randint(0, self.canvas_height - 1 - self.dice_height)
                overlap = False

                top_left_X = left
                top_left_Y = top
                top_right_X = left + self.dice_width
                top_right_Y = top
                bottom_left_X = left
                bottom_left_Y = top + self.dice_height
                bottom_right_X = left + self.dice_width
                bottom_right_Y = top + self.dice_height

                for prev_left, prev_top in dice_top_left_corners:
                    prev_right = prev_left + self.dice_width
                    prev_bottom = prev_top + self.dice_height

                    for corner_X, corner_Y in ((top_left_X, top_left_Y),
                                            (top_right_X, top_right_Y),
                                            (bottom_left_X, bottom_left_Y),
                                            (bottom_right_X, bottom_right_Y)):
                        if (prev_left <= corner_X < prev_right
                            and prev_top <= corner_Y < prev_bottom):
                            overlap = True

                if not overlap:
                    dice_top_left_corners.append((left, top))
                    break

        return dice_top_left_corners
    

    def create_canvas(self):
        self.clear_canvas()
        for pos, (sx, sy) in enumerate(self.dice_top_left_corners):
            for y in range(self.dice_height):
                for x in range(self.dice_width):
                    self.canvas[(sx + x, sy + y)] = self.dice[pos][0][y][x]


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
        '''The method check terminal size and if one of two conditions 
        is not met, the game will not run. 
        First condition: a product of width and height must be greater than or 
        equal to 1200, e. g. 60 columns times 20 lines equals 1200. 
        Second condition:  Either width or height must be greater than 13.'''
        self.clear_screen()
        if (os.get_terminal_size().columns < 14 or 
            os.get_terminal_size().lines < 14):
            print(f'Please resize your terminal window. Minimal lenght of width or height is 14 characters.\nYour dimensions are: width: {os.get_terminal_size().columns} x height: {os.get_terminal_size().lines}')
            sys.exit()
        if (os.get_terminal_size().columns * os.get_terminal_size().lines < 1200):
            print(f'Please resize your terminal window. A product of terminal window dimensions must be at least 1200. Eg. 60 columns times 20 lines = 1200')
            sys.exit()


    def welcome_screen(self):
        '''Welcome player and print initial settings. Ask player if they want to change and return True if so or False if they don't want do any changes.'''

        self.clear_screen()
        print(f'== Welcome to play \'Dicemath\' game =='.center(self.canvas_width), f'''
I will roll the dice and you will try to sum up their values as fast as you can. You have a limited time to do so.
              
Initial settings are: 
Game time: ........ {self.game_duration} seconds
Number of dice: ... {self.dice_number.min} to {self.dice_number.max - 1} dice
              
Do you want to change these settings? type: 'y' or 'yes' to change settings or press Enter to start play''')
        
        if input('> ').lower().startswith('y'):
            return True
        
        return False


    def change_settings(self):
        '''Change game settings, time and number of dice.'''

        self.clear_screen()
        print(' == Game Settings =='.center(self.canvas_width))
        print('How much time you want to have to guess? Enter whole number in seconds, minimum 10, maximum 120.')

        self.game_duration = self.get_limit('time', 10, 120)

        print(f'{'-' * self.canvas_width} ')
        print('How many dice you want to play with? Enter whole numbers, first lower limit, second upper limit. (minimum 1, maximum 8 and the range must be at least 2)')
        
        lower = self.get_limit('lower', 1, 7)
        upper = self.get_limit('upper', lower + 1, 8)

        self.dice_number = DiceNumber(lower, upper)


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
        '''Clear the terminal.'''
        if sys.platform == 'win32':
            subprocess.run('cls')
        else:
            subprocess.run('clear')


    def clear_canvas(self):
        '''Clear canvas.'''
        self.canvas = {}


class Match:
    def __init__(self, game: GameSettings) -> None:
        self.game = game
        self.play_game()


    def sum_up_dice_values(self):
        '''Sum up values of dice in GameSettings.dice variable'''
        total_value = 0
        for _, value in self.game.dice:
            total_value += value
        
        return total_value
        

    def ask_user(self) -> int:
        '''Ask user for the sum of dice values. Check input and return an integer'''
        
        while True:
            user_guess = input('What is the sum? > ')
            if not user_guess.isdecimal() or int(user_guess) < 1:
                print('Enter a whole positive number \033[2A')
                print(' ' * self.game.canvas_width, end='\r')
                continue
            
            print(' ' * self.game.canvas_width)
            return int(user_guess)
    

    def play_game(self):
        while self.game.remaining_time > time():
            self.game.dice = random.choices(dice.ALL_DICE, k=random.randint(self.game.dice_number.min, self.game.dice_number.max))
            self.guess_value = self.sum_up_dice_values()
            self.game.dice_top_left_corners = self.game.distribute_dice(len(self.game.dice))

            self.game.create_canvas()
            self.game.print_canvas()
            
            self.user_guess = self.ask_user()
            
            # print(f'délka canvas: {len(self.game.canvas)}') # DEBUG
            # input() # DEBUG

        # create diceses
        # check if they don't overlap
        # print them on screen
        # let the player answer
        # check for answer and manage points

if __name__ == '__main__':
    new_game = GameSettings()
    new_game.run()