"""CalendarMaker - cvičení z knihy Big book of small projexts
od Al Sweigart. Moje řešení, po projití si cvičení.
Skript vypíše a uloží do textového souboru naformátovaný kalendář 
pro zadaný rok a měsíc"""

# TODO: přidat nastavení formátování

import datetime

DAYS = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']
MONTHS = ['Leden', 'Únor', 'Březen', 'Duben', 'Květen', 'Červen',
          'Červenec', 'Srpen', 'Září', 'Říjen', 'Listopad', 'Prosinec']
layout = 3

def get_calendar(year: int, month: int) -> str:
    """Vrátí textový řetězec zobrazující vybraný měsíc a rok jako kalendář.
    """
    calendar_text = ''
    blank_row = 7 * ('|' + (layout * 3) * ' ') + '|\n'
    split_row = 7 * ('+' + (layout * 3) * '-') + '+\n'
    calendar_text += (MONTHS[month - 1] + ' ' + str(year)).center(layout * 23) + '\n'

    day_label_row = ''
    for day in DAYS:
        if layout == 1:
            day = day[0]
        elif layout == 2:
            day = day[:2]
        day_label_row += '   ' + day.ljust((layout * 3) - 2, ' ')
    day_label_row += ' \n'
    calendar_text += day_label_row

    currentDate = datetime.date(year, month, 1)

    # Jestliže week day není 0 (pondělí) snižuj dokud není pondělí
    while currentDate.weekday() != 0:
        currentDate -= datetime.timedelta(days=1)

    # prochází týdny v měsíci. zastaví se, když se měsíc nerovná zadanemu měsíci
    while True:
        calendar_text += split_row

        day_number_row = ''
        for _ in DAYS:
            day_number = str(currentDate.day).rjust(2)
            day_number_row += '| ' + day_number + ((layout * 3) - 3) * ' '
            currentDate += datetime.timedelta(days=1)
        day_number_row += '|\n'

        calendar_text += day_number_row

        for _ in range(layout - 1):
            calendar_text += blank_row

        if currentDate.month != month:
            break
    
    calendar_text += split_row

    return calendar_text



def get_year() -> int:
    """Získá od uživatele rok a ověří, že vstup je číslo v rozmezí 0 - 9999"""
    print('Zadejte rok ve kterém chcete vytvořit kalendář:')
    year = input(' > ')

    while True:
        if year.isdecimal() and 0 < int(year) <= 9999:
            return int(year)
        else:
            print('Zadejte rok jako celé číslo, např.: "2026"')

def get_month(year: int) -> int:
    """Získá od uživatele měsíc a ověří, že vstup je číslo v rozmezí 1 - 12.
    """

    print(f'Zadejte měsíc pro který chceta v roce {year} vytvořit kalendář:')
    
    while True:
        month = input(' > ')
        if month.isdecimal() and 0 < int(month) <= 12:
            return int(month)
        else:
            print('Zadejte měsíc jako celé číslo, např.: "8" pro "Srpen"')

def get_layout() -> int:
    """Získá od uživatele velikost kalendáře a ověří, že vstup je číslo v rozmezí 1 - 7.
    """

    print(f'Zadejte velikost kalendáře v rozmezí 1 až 7:')
    
    while True:
        layout = input(' > ')
        if layout.isdecimal() and 0 < int(layout) <= 7:
            return int(layout)
        else:
            print('Zadejte velikost jako celé číslo v rozmezí od 1 do 7."')
        
if __name__ == '__main__':
    year = get_year()
    month = get_month(year)
    layout = get_layout()

    calendar = get_calendar(year, month)

    print(calendar)