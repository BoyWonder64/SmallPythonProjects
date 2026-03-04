"""Blackjack, orginally created by Al Sweigart and modifed by Me 
The classic card game also known as 21. (Without spliting or insurance)
"""
import random, sys

# Set up constants

HEARTS = chr(9829) 
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'
CHECKCARDS = ('10', 'J', 'Q', 'K')
FACECARDS = ('J', 'Q', 'K', 'A')

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
    
    money = 5000 # establish players bank. 
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
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()] # Removes 2 cards from end of list
        playerHand = [deck.pop(), deck.pop()]
        
        # Handle the player actions
        print('Bet:', bet)
        while True: # Keep looping until player stands or busts
            displayHands(playerHand, dealerHand, False) # Call displayHands with three arguments
            print()
            
            # Check if player has busts
            if getHandValue(playerHand) > 21:
                break # GAME OVER 
            
            # Get the player's move, either H, S and D:
            move = getMove(playerHand, money - bet)
            
            # Handle the players actions
            if move == 'D':
                # Player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet))) 
                #min returns the smaller of the two values
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)
                
            if move in ('H', 'D'):
                    # Hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)
                
                if getHandValue(playerHand) > 21:
                    # The player has busted:
                    continue
            
            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn.
                break
        
        # Handle the dealer's actions:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer Hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                
                if getHandValue(dealerHand) > 21:
                    break # The dealer has busted.
                input('Press Enter to continue...')
                print('\n\n')
                
            # Show the final hands:
            displayHands(playerHand, dealerHand, True)
            
            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)
            isplayerBlackJack = checkBlackJack(playerHand) # Check if player has blackjack
            isDealerBlackJack = checkBlackJack(dealerHand) # Check if dealer has blackjack
            # Handle whether the player won, lost, or tied
            if isplayerBlackJack == True:
                bet = bet * 10 # You win big!
                money += bet
            elif isDealerBlackJack == True:
                bet = bet * 10 # You lose big!!
                money -= bet
            elif dealerValue > 21:
                print('Dealer busts! You win ${}!'.format(bet))
                money += bet
            elif(playerValue > 21) or (playerValue < dealerValue):
                print('You lost!')
                money -= bet
            elif playerValue > dealerValue:
                print('You won ${}'.format(bet))
                money += bet
            elif playerValue == dealerValue:
                print("It's a tie, the bet is returned to you.")
            
            input('Press Enter to continue...')
            print('\n\n')
            
def getBet(maxBet):
    """Ask the player how much they want to bet for this round"""
    while True: # Keep asking until they enter a valid amount.
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        
        if not bet.isdecimal():
            continue # If the player didn't enter a number, ask again.
        
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Player entered a valid bet. 

def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's 
    first card if showDealerHand is False"""
    print()
    if showDealerHand: # Bool value
        print('DEALER:' , getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])
    
    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)"""
    value = 0
    numberOfAces = 0
    
    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'): # Face cards are worth 10 points
            value += 10
        else:
            value += int(rank) # Numbered cards are worth their number.
        
    # Add the value of the aces:
    value += numberOfAces # Add 1 per ace.
    for i in range(numberOfAces):
        # If another 10 can be added with busting, do so:
        if value + 10 <= 21:
            value += 10
    
    checkBlackJack(cards)
    return value

# Determine if the player has a blackjack
# If their first two cards are an ace of spades and a black jack
def checkBlackJack(cards):
    isBlackJack = False
    if len(cards) == 2:
        rank1 = cards[0][0] # (rank)(suit) == exp: ('A', '♠')
        rank2 = cards[1][0]
        
        # checkCards = ('10', 'J', 'Q', 'K') # we are checking for these cards
        
        if rank1 == 'A' and rank2 in CHECKCARDS:
            isBlackJack = True
        elif rank2 == 'A' and rank1 in CHECKCARDS:
            isBlackJack = True
    
    return isBlackJack
        
def checkFirstTwoPair(cards):
    isFirstTwoaPair = False
    if len(cards) == 2:
        rank1 = cards[0][0]
        rank2 = cards[1][0]
        
        if rank1 in CHECKCARDS and rank2 in CHECKCARDS: 
            if rank1 == rank2:
                isFirstTwoaPair = True
        if rank1 not in FACECARDS and rank1 == rank2:
                isFirstTwoaPair = True
    return isFirstTwoaPair
            
            

def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', ''] # The text to display on each row
    
    for i, card in enumerate(cards):
        rows[0] += ' ___ ' # Print the top line of the card
        if card == BACKSIDE:
            # Print a cards back:
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '| ##|'
        else:
            # Print the card's front:
            rank, suit = card # The card is a tuple data structures
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2, '_'))
    
    # Print each row on the screen
    for row in rows:
        print(row)
        
def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down."""
    while True: # Keep looping until the player enters a correct move.
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']
        
        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
            
        # Get the player's move:
        movePrompt = ', '.join(moves) + '> ' # combine all moves
        move = input(movePrompt).upper() # Format them 
        if move in ('H', 'S'): # Check what move the player gave us
            return move # The player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move # Player has entered a valid move
        
# if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()