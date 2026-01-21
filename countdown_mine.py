"""Simple count down timer.
Inspired by Al Sweigart's book 'The Big Book of Small Pyton Projects': 
https://inventwithpython.com/bigbookpython/project13.html
Writen from scratch using OOP concept as an excercise."""

import sys
import os
import time
import sevseg_mine

def get_seconds() -> int:
    """Get second from user. Check if it is correct input and return an int."""
    while True:
        seconds = input('Počet sekund k odpočtu: ')
        if seconds.isdecimal():
            return int(seconds)
        

def run_timer(seconds_left: int) -> None:
    try:
        while True:
            os.system('clear')
            hours = seconds_left // 3600
            minutes = (seconds_left % 3600) // 60
            seconds = seconds_left % 3600

            h_string = sevseg_mine.get_sev_seg_string(hours, 2)
            h_top, h_middle, h_bottom = h_string.splitlines()

            m_string = sevseg_mine.get_sev_seg_string(minutes, 2)
            m_top, m_middle, m_bottom = m_string.splitlines()

            s_string = sevseg_mine.get_sev_seg_string(seconds, 2)
            s_top, s_middle, s_bottom = s_string.splitlines()

            print(h_top    + '     ' + m_top    + '     ' + s_top)
            print(h_middle + '  *  ' + m_middle + '  *  ' + s_middle)
            print(h_bottom + '  *  ' + m_bottom + '  *  ' + s_bottom)

            if seconds_left == 0:
                print()
                print('                          ')
                print('  .    .  *  .  *     *    *   ')
                print('    .  *   *  bOOOOm     *  *  ')
                print('  *      *  *    .  *  *   *   ')
                break

            seconds_left -= 1
            time.sleep(1)

    except KeyboardInterrupt:
        print('\nBye bye.')

if __name__ == '__main__':
    seconds = get_seconds()
    run_timer(seconds)