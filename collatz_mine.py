"""Collatz Sequence / inspired by Al Sweigart (Big Book of Small Projects)
Skript vygeneruje seqenci čísel podle Collatzova problému,
graficky znázorní jednotlivé kroky a vypíše počet kroků pro prvních -n číslic
autor: Lukáš Karásek
GitHub: https://github.com/ArseneLuko
"""

import os
import time

def get_number() -> int:
    """Vyžádá vstup od uživatele a vrátí jej jako celé číslo větší než nula."""

    print('Zadej číslo pro které chceš generovat Collatzovu sekvenci:')
    while True:
        
        response = input(' > ')

        if not response.isdecimal() or response == '0':
            print('Zadej celé číslo větší než 0.')
            continue
        else:
            break

    return int(response)

def get_sequence(starting_number: int) -> list:
    """Vygeneruje Collatzovu sekvenci pro zadané číslo."""
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

def print_sequence(sequence: list) -> None:
    print(sequence[0], end='')
    for n in sequence[1:]:
        print(f', {n}', end='', flush=True)
        time.sleep(0.08)
    print()

def main():
    os.system('clear')
    print('Collatz sequence generátor'.center(52))
    print('-' * 52)
    starting_number = get_number()
    print(f'Collatz sequence pro číslo: {starting_number}')
    sequence = get_sequence(starting_number)
    print_sequence(sequence)


if __name__ == '__main__':
    main()