"""Collatz Sequence / inspired by Al Sweigart (Big Book of Small Projects)
Skript vygeneruje seqenci čísel podle Collatzova problému,
graficky znázorní jednotlivé kroky a vypíše počet kroků pro prvních -n číslic
autor: Lukáš Karásek
GitHub: https://github.com/ArseneLuko
"""

import os
import sys
import time

n = 1000000
CHOICES = ('volby', 'help', 'man', 'v', '?')
QUITS = ('quit', 'konec', 'k', 'q', 'x')


def get_input() -> int:
    """Vyžádá vstup od uživatele a vrátí jej jako celé číslo větší než nula."""

    print('Zadejte číslo pro které chcete generovat sekvenci:')

    while True:
        response = input(' > ')
        if not response.isdecimal() or response == '0':
            print('Zadejte celé číslo větší než 0.')
            continue
        else:
            break

    return int(response)


def get_sequence(starting_number: int) -> list:
    """Vygeneruje Collatzovu sekvenci pro zadané číslo a vrátí jako list"""
    n = starting_number
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0: # sudé, even, cho
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence
    # return [3, 10, 5, 16, 8, 4, 2, 1] # testing line


def one_sequence() -> None:
    """Vygeneruje seqenci pro zadané číslo a zobrazí"""

    starting_number = get_input()

    print(f'Collatz sequence pro číslo: {starting_number}')
    sequence = get_sequence(starting_number)

    print_sequence(sequence)
    print(f'Délka sekvence: {len(sequence)}')


def count_steps(amount: int) -> None:
    """Vytvoří sekvenci pro prvních n-čísel (implicitně 100) a vypíše délku sekvencí"""

    steps = {
        'maximum': 0,
        'number': 0
    }

    for step in range(1, amount + 1):
        sequence = get_sequence(step)
        print(f'Počet kroků pro číslo {step} je {len(sequence)}')
        if len(sequence) > steps['maximum']:
            steps['maximum'] = len(sequence)
            steps['number'] = step

    print(f'Nejdelší sekvenci v prvních {amount} číslech má číslo {steps['number']}. Jeho sekvence má {steps['maximum']} kroků.')


def print_sequence(sequence: list) -> None:
    print(sequence[0], end='')
    for n in sequence[1:]:
        print(f', {n}', end='', flush=True)
        time.sleep(0.08)
    print()


def print_choices(starting_number: int) -> None:
    print('Collatz sequence generátor'.center(52))
    print('-' * 52)
    print(f'  1 | Vygeneruje sekvenci pro zadané číslo')
    print(f'  2 | Zobrazit graficky kroky sekvence pro vybrané číslo')
    print(f'  3 | Vypsat délku sekvencí pro prvních {n} čísel')
    print(f'  k | Ukončí skript')


def main():
    starting_number = 'n/a'
    print_choices(starting_number)
    
    while True:
        print('-' * 52)
        print('Vyberte volbu z menu')
        choice = input(' > ')
        if choice.isdecimal() and int(choice) in range(1, 4):
            if int(choice) == 1:
                starting_number = one_sequence()
            if int(choice) == 2:
                print('volba 2')
            if int(choice) == 3:
                count_steps(n)
        elif choice in (CHOICES):
            print_choices(starting_number)
        elif choice in (QUITS):
            sys.exit()
        else:
            print('Vyberte jednu z možností výše, zadejte číslo volby.')
            print('Pro vypsání možností zadejte: \'?\'')


if __name__ == '__main__':
    os.system('clear')
    main()