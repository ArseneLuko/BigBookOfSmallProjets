"""Conway's Game of Life, by Al Sweigart al@inventwithpython.com
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/conway%27s_Game_of_Life
This code available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, simulation"""

import copy, random, sys, time

# Set up the constatns:
WIDTH = 79 # The width of the cell grid
HEIGHT = 20 # The height of the cell grid

# (!) Try to change ALIVE to '#' or another character:
ALIVE = 'O' # The character representing a living cell
# (!) Try to change DEAD to '.' or another character:
DEAD = ' '

# Try changing ALIVE to '|' and DEAD to '-'

# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values
nextCells = {}
# Put random dead and alive cells into nextCells:
for x in range(WIDTH): # Loop over every possible column
    for y in range(HEIGHT): # Loop over every possible row
        # 50/50 chance for starting cells being alice or dead
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE # Add a living cell
        else:
            nextCells[(x, y)] = DEAD  

while True: # Main program loop
    # Each iteration of this loop is a step of the simulation
    
    print('\n' * 50) # Separate each step with new lines
    cells = copy.deepcopy(nextCells)

    # Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print() # Print a newline at the end of the row
    print('Press Ctrl-C to quit.')

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates (x, y), even if they
            # wrap around the edge:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1 # Top left neighbor is alive.
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1 # Top neighbor is alive.
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1 # Top right neighbor is alive.
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1 # Left neighbor is alive.
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1 # Right neighbor is alive.
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1 # Bottom left neighbor is alive.
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1 # Bottom neighbor is alive.
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1 # Bottom right neighbor is alive.

            # Set cel5l based on Conway's Game of Life rules:
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 
                or numNeighbors == 3):
                # Living cell with 2 or 3 neighbors stay alive.
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # Dead cell with 3 neighbor become alive
                nextCells[(x, y)] = ALIVE
            else:
                # Everything else dies or stays dead:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(.01) # Add a 1 second pause to reduce flickering
    except KeyboardInterrupt:
        print('Conway\'s Game of Life')
        print('By Al Sweigart al@inventwithpython.com')
        sys.exit() 