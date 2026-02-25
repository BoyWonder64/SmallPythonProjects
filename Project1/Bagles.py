import random

NUM_DIGITS = 3 # Try setting this to a number between 1 and 10
MAX_GUESSES = 10 # Try setting this to a number between 1 and 100

def main():
    print('''Bagels, a deductive logic game.
          Credit to Al Sweigart
          
          I am thinking of a {}-digit number with no repeated digits
          Try to guess what it is. Here are some clues. 
          When I say:           That means:
          Pico                  One digit is correct but in the wrong position
          Fermi                 One digit is correct but in the right position
          Bagles                No digit is correct.
          
          For example, if the secret number was 248, and your guess was 843, the clues would be
          Fermi Pico. '''.format(NUM_DIGITS))
    
    while True: # Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought of a number')    
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break # They figured it out, we need to break out of the loop
            if numGuesses > MAX_GUESSES:
                print('You have ran out of guesses.')
                print('The answer was {}'.format(secretNum))
        
        # Ask player if they want to play again
        print('Would you like to play again? (Yes or No)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing! Have a good day')
        
    
def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9
    random.shuffle(numbers) # Shuffle them into random order.
        
    # Get the first NUM_DIGITS digits in the list for the secret number
        
    secretNum = ''
    for i in range (NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
    
def getClues(guess, secretNum):
    """Returns a string with pico, fermi, bagles clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the correct place
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagles' # There are no correct digits at all.
    
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make single string from the list of string clues. 
        return ' '.join(clues)
    
    # If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
    
    
# Test your knowledge:

# What happens if you modify NUM_DIGITS: 
    # The number of digits I have to guess increases

# What happens if you set NUM_DIGITS to something larger than 10:
    # That list index becomes out of range because their isn't 10+ items in the list
    
# What happens if you set secretNum = 123
    # Then the number you have to guess will always be 123
    
# What happens if you delete or comment out numGuesses 
    # the value doesnt exisit and you are unable to use it as an argument. 
    
# What happens if you delete or comment out random.shuffle(numbers)
    # The list is no longer shuffled and will always select the first three numbers which in our case is 012

# What happens if you comment out if guess == secretNum: return 'You got it!'
    # Then when you are correct the game doesnt end

# What happens if you comment out   numGuesses += 1
    # You have unlimited guesses. 