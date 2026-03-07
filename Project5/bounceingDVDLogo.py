""" Bouncing DVD Logo, designed by AL Sweigart and updated my ME
A bouncing DVD logo animation. You have to sorta be a certain age
to appreciate this. Press Ctrl-C to stop the program.

NOTE: Please do not resize the terminal whindow while the program is running"""

import sys, random, time

try:
    import bext
except ImportError:
    print("ERROR: This program requires the bext module")
    print('Install it by following the instructions at')
    print('https://pypi.org/project/Bext')
    print('Good bye!')
    sys.exit()
    
# Establish Constants
WIDTH, HEIGHT = bext.size()

# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

NUMBER_OF_LOGOS = 5 # (!) Feel free to change this to any value from 1 to 100
PAUSE_AMOUNT = 0.2 # (!) Feel free to change this is any value like 1.0 or 0.0
# (!) Try changing this list to fewer colors if you want
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT  = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS), 
                     X: random.randint(1, WIDTH - 4),
                     Y: random.randint(1, HEIGHT - 4),
                     DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # Make sure X is even so it can hit the corner
            logos[-1][X] -= 1
        
        cornerBounces = 0 # Track how many times the logo hits a corner
        while True:
            # Main Loop beings here.
            for logo in logos: # Handle each logo in the logos list
                # Erase the logo's current location:
                bext.goto(logo[X], logo[Y])
                print('   ', end='') # (!) Try commenting this line out for funsies

                originalDirection = logo[DIR]

                # See if the logo bounces off the corners:
                if logo[X] == 0 and logo[Y] == 0:
                    logo[DIR] = DOWN_RIGHT
                    cornerBounces += 1
                elif logo[X] == 0 and logo[Y] == HEIGHT -1:
                    cornerBounces += 1
                elif logo[X] == WIDTH -3 and logo[Y] == 0:
                    cornerBounces += 1
                elif logo[X] == WIDTH -3 and logo[Y] == HEIGHT -1:
                    logo[DIR] = UP_LEFT
                    cornerBounces += 1

                # See if the logo bounces off the left edge:
                
