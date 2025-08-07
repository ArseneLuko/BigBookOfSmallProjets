"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short"""

import datetime

# Set up the constants
DAYS = ('Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle')

MONTHS = ('Leden', 'Únor', 'Březen', 'Duben', 'Květen', 'Červen', 'Červenec',
          'Srpen', 'Září', 'Říjen', 'Listopad', 'Prosinec')

print('Vytvoř kalendář / inspirováno Al Sweigart al@inventwithpython.com')

while True: # Get a year from user
    print('Zadejte rok kalendáře:')
    respons = input('> ')

    if respons.isdecimal() and int(respons) > 0:
        year = int(respons)
        break

    print('Zadejte rok jako číslo, napříkla: 2025.')
    continue

while True: # Get a month from user
    print('Zadejte měsíc, jako číslo 1–12:')
    respons = input('> ')

    if not respons.isdecimal():
        print('Zadejte měsíc jako číslo, například 8 pro Srpen.')
        continue
    
    month = int(respons)
    if 1 <= month <= 12:
        break

    print('Zadejte číslo mezi 1 až 12')


def getCelendarFor(year: str, month: str) -> str:
    calText = '' # the string for calendar

    # Put the month and year at the top of the calendar
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # add the days of the week labels to the calendar
    # try changing tgis to abbreviations: Po, Út,... 
    calText += '...Pondělí....Úterý......Středa.....Čtvrtek....Pátek......Sobota.....Neděle...\n'

    # The horizontal string that separates weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separator
    blankRow = ('|          ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all
    # the comlicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)

    # Roll back currentDate until it is Sunday (weekday() returns 6
    # for Sunday, - starts with 0 from Monday)
    while currentDate.weekday() != 0: # Lukáš, změna na 0 -> začíná pondělí
        currentDate -= datetime.timedelta(days=1)

    while True: # loop over each week in the month
        calText += weekSeparator

        #dayNumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n' # add the vertical line after sunday

        # add the day number row and 3 blank rows to the calendar text
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        # check if we are done with the mont
        if currentDate.month != month:
            break

    # add the horizontal line at the very bottom of the calendar
    calText += weekSeparator
    return calText
    
if __name__ == '__main__':
    calText = getCelendarFor(year, month)
    print(calText)

    # Save the calendar to a text file:
    celendarFilename = f'kalendar_{year}_{month}.txt'
    with open(celendarFilename, 'w') as fileObj:
        fileObj.write(calText)

    print(' Saved to ' + celendarFilename)