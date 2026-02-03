import random
import time
import sys

WIDTH = 70
SPACE = 10

L_CHAR = '>'
R_CHAR = '<'
S_CHAR = ' '

PAUSE = 0.1

DIRECTIONS = (-1, 1)

def asembly_line(left_side):
    right_side = WIDTH - SPACE - left_side

    final_line = (left_side * L_CHAR) + (SPACE * S_CHAR) + (right_side * R_CHAR)

    return final_line

def new_shift(left_side):
    dir = random.choice(DIRECTIONS)

    if (left_side + dir == 0) or (left_side + dir + SPACE == WIDTH):
        return left_side

    return left_side + dir   

def run():
    left_side = random.randint(1, WIDTH - SPACE)
    while True:
        try:
            time.sleep(PAUSE)
        except KeyboardInterrupt:
            sys.exit()

        print(asembly_line(left_side))
        left_side = new_shift(left_side)
        

if __name__ == '__main__':
    run()
