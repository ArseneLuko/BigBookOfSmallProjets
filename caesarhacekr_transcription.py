"""Caesar Ciper Hacker, by Al Sweigart al@inventwithpyton.com
This programs hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
More info at:
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

# Let the user specify the message to hack:
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ').upper()


# Every possible symbol that can be enc/dec
# This must match the SYMBOLS used when encrypting the message
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): 
    translated = ''

    # Decrypt each symbol in the message
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key

            # wrap-around handle
            if num < 0:
                num = num + len(SYMBOLS)

            # add decrypted number symbol to translated
            translated = translated + SYMBOLS[num]
        else:
            # just add original symbol
            translated = translated + symbol

    # display the key being tested, along with its decrypted text
    print(f'Key #{key}: {translated}')
    