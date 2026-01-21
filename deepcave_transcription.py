"""Deep Cave, by Al Sweigart, al@inventwithpython.com
An animation of a deep cave that goes forever into the earth.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, scrolling, artistic"""


import random, sys, time

# Set up the constants:
WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Deep Cave, vy Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
# time.sleep(2)

left_width = 20
gap_width = 10

while True:
    # Display the tunel segment
    right_width = WIDTH - gap_width - left_width
    print(('>' * left_width) + ('.' * gap_width) + ('<' * right_width))

    # Check for Ctkl-C press during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit('\nBye bye')

    # Adjust the left side width:
    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and left_width > 1:
        left_width -= 1
    elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
        left_width += 1
    else:
        pass