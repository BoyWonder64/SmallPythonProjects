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
