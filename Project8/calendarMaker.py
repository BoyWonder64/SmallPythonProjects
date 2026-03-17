"""Calendar Maker by Me 
Create monthly calendars, saved to a text file and fit for printing."""

import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Mr')

while True: # Loop to get a year from the user
    print('Please enter a year for the calendar:')
    response = input('> ')
    
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    
    print('Please enter a numeric year, like 2026')
    continue

while True: # Loop to get a month from the user
    print('Please enter a month for the calendar, 1-12:')
    response = input('< ')
    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March')
        continue
    
    month = int(response)
    if 1 <= month <= 12:
        break
    
    print('Please enter a number from 1 to 12')
    
    
def getCalendarFor(year, month):
    calText = '' # calText will contain the string of our calendar
    
    # Add the days of the week labels to the calendar
    # (!) Try chaning these to abbreviations:
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    
    # The horizontal line string that separate weeks:
    weekSeparator = ('+----------' * 7) + '\n'
    
    # The blank rows have ten spaces in between the | day separators:
    blankRow = ('|           ' * 7) + '|\n'
    
    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)
    
    # Roll back currentDate until it is Sunday. (weekday() returns 6
    # for Sunday not 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
        
    while True: # Loop over each week in the month
        calText += weekSeparator
        
        # dayNumberRow is a row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)