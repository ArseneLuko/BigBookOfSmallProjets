"""Dice Math, by Al Sweigart al@inventwithpython.com
A flash card addition game where you sum the total on random dice rolls.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, game, math"""

import random, time

# Set up the constants
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3 # -3 for room to enter the sum at the bottom

# The diration is in seconds:
QUIZ_DURATTION = 30
MIN_DICE = 2
MAX_DICE = 6

# (!) Try changing these to different numbers:
REWARD = 4
PENALTY = 1



# The program hangs if all of the dice can't fit on the screen
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2A = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2B = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3A = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3B = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6A = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6B = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2A, D2B, D3A, D3B, D4, D5, D6A, D6B]

print('''Dice Math, by Al Sweigart al@inventwithpython.com
      
Add up the sides of all the dice displayed on the screen. You have
{} seconds to answer as many as possible. You get {} points for each
correct answer and lose {} point for each incorrect answer.
'''.format(QUIZ_DURATTION, REWARD, PENALTY))
input('Press Enter to begin...')

# Keep track of how many answers ware correct and incorrect:
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATTION:
    # Come up with the dice to display:
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        # die[0] contains the list of strings of the die face:
        diceFaces.append(die[0])
        # die[1] contains the integer number of pips on the face:
        sumAnswer += die[1]
    
    # Contains (x, y) tuples of the top-left corner of each die.
    topLeftDiceCorner = []

    # Figure out where dice should go:
    for i in range(len(diceFaces)):
        while True:
            # Find a random place on the canvas to put the die
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # Get the x, y coordinates for all four corners:
            #       left
            #       ∨
            # top > +-------+  ∧
            #       | O     |  |
            #       |   O   |  | DICE_HEIGHT (5)
            #       |     O |  |
            #       +-------+  ∨
            #       <------->
            #       DICE_WIDTH (9)
            topLeftX = left
            topLeftY = top
            topRigthX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # Check if this die overlaps with previous dice.
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorner:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT
                # Check each corner of this die to see if it is inside
                # of the area the previous dies:
                for cornerX, cornerY in ((topLeftX, topLeftY),
                                         (topRigthX, topRightY),
                                         (bottomLeftX, bottomLeftY),
                                         (bottomRightX, bottomRightY)):
                    if (prevDieLeft <= cornerX < prevDieRight
                        and prevDieTop <= cornerY < prevDieBottom):
                        overlaps = True

            if not overlaps:
                # 
                topLeftDiceCorner.append((left, top))
                break

    # Draw the dice on the canvas:

    # Keys are (x, y) tuples of ints, values the character at that
    # position on the canvas:
    canvas = {}
    # Loop for each die:
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorner):
        #Loop over each character in the die's face:
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # Copy this character to the correct place on the canvas:
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                # Note that in dieFace, a list of strings, the x and y
                # are swapped:
                canvas[(canvasX, canvasY)] = dieFace[dy][dx]

    # Display the canvas on the screen:
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()

    # Let the player enter their answe
    response = input('Enter the sum:').strip()
    if response.isdecimal and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print('Incorrect, the answer is', sumAnswer)
        time.sleep(2)
        incorrectAnswers +=1

# Display the final score:
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct:'.ljust(11), correctAnswers)
print('Incorrect:'.ljust(11), incorrectAnswers)
print('Score:'.ljust(11), score)



				


