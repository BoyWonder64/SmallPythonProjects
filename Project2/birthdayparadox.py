"""Birthday Paradox Simulation, orginally designed by Al Sweigart and modifed by me
Explore the surprising probabilites of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem"""

import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []

    for i in range (numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all 
        # birthdays have the same year.
        startOfYear = datetime.date(2000, 1, 1)
        
        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
        
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once 
    in the birthday list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays happened to be unique, so we return none 
    
# Display the intro
print(''' Birthday Paradox by yours truely
      The  Birthday Paradox shows us that in a group of N people the odds
      that two of them have matching birthdays is surprisingly large. 
      This program does a Monte Carlo simulation (that is, repeated random simulations)
      to explore this concept
      
      (Fun fact: Its not actually a paradox, its just a suprising result)
      ''')

# Set up a tuple of month names in order: 
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # Keep asking until the user gives us good input.
    print('How many birthdays shall I generate (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100): # if the response is a decimal and its greater than 0 and less or equal to 100
        numBDays = int(response) # convert response into an int and store it into numBDays
        break # User has given us a valid response, lets move on
print()

# Generate and display the birthdays
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
        monthName = MONTHS[birthday.month -1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
    print()
    print()
    
# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Multiple people have a birthday on', dateText)
    
else:
    print('There are no matching birthdays') 
print()

# Run through 100,000 simulations
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let/s run another 100,000 simulations.')
simMatch = 0 # How many simulations had matching birthdays in them
for i in range(100_000):
    # Report on the progress every 10,000 simulations
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Display the results: 
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a ', probability, '% chance of')
print('having a matching birthday in their group.')
print('Thats\'s probably more than you would think!')
        
        
    
   