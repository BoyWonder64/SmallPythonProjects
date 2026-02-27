"""Bitmap Message, orginally designed by Al Sweigart and modifed by me
Displays a text message according to the provided bitmap image.
More info at https://en.wikipedia.org/wiki/Birthday_problem"""

import sys


# There are 68 periods along the top and bottom of this string:
bitmap = """
14. ....................................................................
15.    **************   *  *** **  *      ******************************
16.   ********************* ** ** *  * ****************************** *
17.  **      *****************       ******************************
18.           *************          **  * **** ** ************** *
19.            *********            *******   **************** * *
20.             ********           ***************************  *
21.    *        * **** ***         *************** ******  ** *
22.                ****  *         ***************   *** ***  *
23.                  ******         *************    **   **  *
24.                  ********        *************    *  ** ***
25.                    ********         ********          * *** ****
26.                    *********         ******  *        **** ** * **
27.                    *********         ****** * *           *** *   *
28.                      ******          ***** **             *****   *
29.                      *****            **** *            ********
30.                     *****             ****              *********
31.                     ****              **                 *******   *
32.                     ***                                       *    *
33.                     **     *                    *
34. ...................................................................."""

print('Welcome to Bitmap Message!')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()
    
# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # print an empty space since theres a space in the bitmap:
            print (' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print() # Print a newline
