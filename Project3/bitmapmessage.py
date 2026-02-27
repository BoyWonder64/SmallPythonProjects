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
for line in bitmap.splitlines(): # Splits a big multi-line string into a list of lines. example: ['***', '* *', '***']
    # Loop over each character in the line:
    for i, bit in enumerate(line): #enumerate takes the list we created and enumerates them: ['***'] = [(0,'*'),(1,'*'),(2,'*')]
        '''line = "DOG"

            for i, bit in enumerate(line):
                print("Index:", i, "Character:", bit)
                ***********************************
                Index: 0 Character: D
                Index: 1 Character: O
                Index: 2 Character: G
                ***********************************
                '''
                
        if bit == ' ':
            # print an empty space since theres a space in the bitmap:
            print (' ', end='') # A normal print once finished will end include by default '/n' example print('Yo what up', end='/n') but 
            # if we change the value to end='' we stay on the same line. 
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='') # i % len(message) means: Keep i between 0 and the last index of the message
            # if message = cat then lenth of message is 3 (length starts counting at 1) and therefore if the line is dogdogdogdog the index count is = 11
            # therefore the printing logic is: 
            '''
            0 % 3 = 0  = d
            1 % 3 = 1  = 0
            2 % 3 = 2  = g
            3 % 3 = 0  = d
            4 % 3 = 1  = o
            5 % 3 = 2  = g
            6 % 3 = 0  = d
            7 % 3 = 1  = o
            8 % 3 = 2  = g
            '''
    print() # Print a newline

# What happens if the player enters a blank string for the message?
    # the program exits
    
# Does it matter what the nonspace characters are in the bitmap variables string?
    # no, regardless of what it see, its just counting if something is there or not, were not scanning
    # for *, this is why the map also prints characters for the header and footer

# what does the i variable on line 41 represent
    # the index
    
# What bug/happens if you delete the final line print()
    # the bitmap output doesnt create a newline and so it will being the next message on the same line
    # until the terminal forces a new line and therefore the message becomes jumbled. 