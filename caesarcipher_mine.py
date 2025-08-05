"""Caesar Cipher - inspired by Al Sweigart from 'Big book of small projects'
The script encrypt (or decrypt) text by shifting letters over by a key number. For example, a key of 2 means the letter A is encrypted into C, the letter B encrypted into D, and so on. Works with english alphabet only."""

alphabet = [l for l in 'abcdefghijklmnopqrstuvwxyz']

def encrypt(text: str, key: int) -> str:
    """Returns encrypted string with letters shifted over by a key"""
    encrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        encrypted_text += alphabet[(position + key) % len(alphabet)]
    return encrypted_text

def decrypt(text: str, key: int) -> str:
    """Return decrypted string based on a key"""
    decrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        decrypted_text += alphabet[(position - key) % len(alphabet)]
    return decrypted_text

def control_key(key: int) -> bool:
    """Checks whether the given input is an integer"""
    try:
        key = int(key)
    except ValueError:
        return False
    else:
        if key in range(0, 25):
            return True
        else:
            return False

def main():
    """Main program loop"""
    print("""
Caesar Cipher - inspired by Al Sweigart from 'Big book of small projects'
The script encrypt (or decrypt) text by shifting letters over by a key number.
For example, a key of 2 means the letter A is encrypted into C, the letter B
encrypted into D, and so on. Works with english alphabet only.
          """)
    
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    while True:  
        respons = input(" > ")
        if respons in ('e', 'E', 'd', 'D'):
            break
        print("Pleasy enter only 'e' or 'd'")

    print("Enter the key (0 to 25) to use")
    while True:
        key = input(" > ")
        if control_key(key):
            key = int(key)
            break
        print("Please enter an integer in the range from 0 to 25 ")


    print("Enter the text to work with:")
    text = input(" > ")

    if respons.lower() == 'e':
        result = encrypt(text, key)
    elif respons.lower() == 'd':
        result = decrypt(text, key)

    print(result)

    


if __name__ == "__main__":
    main()