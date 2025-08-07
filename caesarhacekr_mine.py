SYMBOLS = [l for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

def brute_force(text: str) -> str:
    for key in range(len(SYMBOLS)):
        decrypted_text = ""
        for letter in text:
            if letter.upper() in SYMBOLS:
                position = SYMBOLS.index(letter)
                decrypted_text += SYMBOLS[(position - key) % len(SYMBOLS)]
            else:
                decrypted_text += letter
        print(f'{key} // {decrypted_text}')


def main():
    print('Enter the encrypted Caesar cipher messafe to hack')
    message = input(' >').upper()

    brute_force(message)


if __name__ == '__main__':
    main()