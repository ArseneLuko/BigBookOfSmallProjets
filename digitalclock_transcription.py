"""Digital Clock, by Al Sweigart al@inventwithpython.com
Displays a digital clock of the current time with a seven-segment
display. Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Seven-segment_display
Requires sevseg.py to be in the same folder.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic"""

import sys, time
import sevseg_transcription

try:
    while True:
        # cls screen
        print('\n' * 60)

        # get the current time
        current_time = time.localtime()
        # % 12 so we use a 12-hour clock, not 24
        hours = str(current_time.tm_hour % 12)
        if hours == '0':
            hours = '12' # 12-hour clocks show 12, not 00
        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)

        # 
        h_digits = sevseg_transcription.getSevSegStr(hours, 2)
        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

        m_digits = sevseg_transcription.getSevSegStr(minutes, 2)
        m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

        s_digits = sevseg_transcription.getSevSegStr(seconds, 2)
        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

        # Display the digits
        print(h_top_row     + '   ' + m_top_row    + '   ' + s_top_row)
        print(h_middle_row  + ' * ' + m_middle_row + ' * ' + s_middle_row)
        print(h_bottom_row  + ' * ' + m_bottom_row + ' * ' + s_bottom_row)
        print()
        print('Press Ctrl-C to quit.')

        # Keep looping until the seconds changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != current_time.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by Al Sweigart al @inventwithpython.com')
    sys.exit() 