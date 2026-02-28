"""Blackjack, orginally created by Al Sweigart and modifed by Me 
The classic card game also known as 21. (Without spliting or insurance)
"""
import random, sys

# Set up constants

HEARTS = chr(9892) 
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def main():
    print('''Welcome to Blackjack!
          Rules:
          Try to get as close as possible to 21 (yes like the move lol, just without Kevin Spacey this time)
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points
          Cards 2 through 10 are worth their face value
          (H)it to take another card.
          (S)tand to stop taking cards.
          On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17''')
    
    money = 5000
    while True: # Main game loop
        # Check if the player has any money before proceeding
        if money <= 0:
            print('You\'re broke! GO HOME!')
            print('Just kidding, its not real money')
            print('Thanks for playing')
            sys.exit()
            
        # If we are this far, the player has money
        # Lets have the player made a bet 
        
        print('Money:', money)
        bet = getBet(money)
        
        # Give the dealer and player two cards from the deck each:
        deck = getBet(money)
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        
        # Handle the player actions
        print('Bet:', bet)
        