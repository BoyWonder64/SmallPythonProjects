"""Carrot in a Box by Me by Me
A silly bluffing game between two human players. Based on the game
from the show 8 Out of 10 Cats"""

import random

print('''Carrot in the Box
      
      This is a bluffing game for two human players. Each player has a box
      one box has a carrot in it. To win, you must have the box with the
      carrot in it.
      
      This is a very simple and silly game.
      
      The first player looks into the box (the second player must close
      their eyes during this) The first player then says "Their is a carrot in 
      my box" or "their is not a carrot in my box". The second player then gets
      to decide if they want to swap boxes or not''')

input('Press Enter to begin...')

p1Name = input('Player 1: What is your name:')
p2Name = input('Player 2: What is your name:')
playerNames = p1Name[:11].center(11) + '   ' + p2Name[:11].center(11)

print('''HERE ARE TWO BOXES
      
      _______________            _______________  
    /              / |         /              / |    
   +--------------+  |        +--------------+  |
   |      RED     |  |        |     GOLD     |  |
   |      BOX     | /         |      BOX     | /
   +--------------+/          +--------------+/''')

print()
print(playerNames)
print()
print(p1Name + ', you have a RED box in front of you')
print(p2Name + ', you have a GOLD box in front of you')
print()
print(p1Name + ', you will get you look into your box')
print(p1Name.upper() + ', close your eyes and don\'t look!!!')
input('When' + p2Name + 'has closed their eyes, press Enter...')
print()

print(p1Name + 'here is the inside of the box')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True