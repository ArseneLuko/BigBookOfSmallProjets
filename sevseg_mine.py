digits = {
    '0': """
 __ 
|  |
|__|""",
    '1': """
    
   |
   |""",
    '2': """
 __ 
 __|
|__ """,
    '3': """
 __ 
 __|
 __|""",
    '4': """
    
|__|
   |""",
    '5': """
 __ 
|__ 
 __|""",
    '6': """
 __ 
|__ 
|__|""",
    '7': """
 __ 
   |
   |""",
    '8': """
 __ 
|__|
|__|""",
    '9': """
 __ 
|__|
 __|""",
}

def thousand_sep(number, number_str: str=None):
    """Prepare the number in string format to be added thousand separator.
    
    :param number: number int or float
    :param number_str: string of the number"""
    if not number_str:
        number_str = str(number)

    if isinstance(number, float):
        before, after = number_str.split(".")
        before_rev = before[::-1]

        new_before_rew = add_spaces(before_rev)
        new_after = add_spaces(after)

        result = new_before_rew[::-1] + '.' + new_after

    else:
        before_rev = number_str[::-1]

        new_before_rew = add_spaces(before_rev)

        result = new_before_rew[::-1]

    return result


def add_spaces(string: str, separator: str=" ", every: int=3) -> str:
    """Add separator character to a string on every 3rd place.
    
    :param string: String to be changed
    :param separator: A character to separate groups of characters
    :param every: Size of each block of characters (3 is deafult value
        as thousand separator)
        
    :returns separated_string: string contains a separator every n-th character"""
    separated_string = ''

    for pos, char in enumerate(string):
        if pos % every == 0 and pos != 0:
            separated_string += separator + char
        else:
            separated_string += char

    return separated_string
    

def get_sev_seg_string(symbol: int | float, min_width: int=0, thousands_sep: bool=False) -> str:
    """Return string represent provided number.

    :param number: Number to be converted. Can be int or float
    :param min_width: Number of digits in the provided result. 
        Count all digits before and after decimal point together and the 
        decimal point itself. So `42.0` with 5 digits will be `042.0`.
    :param thousands_sep: If true the return will be separated by a space
        into thousands.
    
    :return String: Return string contains joined 3 rows."""

    rows = ['','','']

    if isinstance(symbol, (int, float)):
        symbol_str = str(symbol)
    else:
        raise TypeError(f"Wrong parameter 'symbol', must be type of int or float.")
    
    if len(symbol_str) < min_width:
        missing = min_width - len(symbol_str)
        symbol_str = missing * "0" + symbol_str

    if thousands_sep:
        symbol_str = thousand_sep(symbol, symbol_str)

    for char in symbol_str:
        if char == ".":
            rows[0] += '  '
            rows[1] += '  '
            rows[2] += ', '
        elif char == " ":
            rows[0] += '   '
            rows[1] += '   '
            rows[2] += '   '
        elif char == "0":
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif char == "1":
            rows[0] += '   '
            rows[1] += ' /|'
            rows[2] += '  |'
        elif char == "2":
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif char == "3":
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif char == "4":
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif char == "5":
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif char == "6":
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif char == "7":
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif char == "8":
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif char == "9":
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'
    
    return "\n".join(rows)


if __name__ == "__main__":
    fourty_two = get_sev_seg_string(1231451678.22345678, thousands_sep=True)
    print(fourty_two)
    print()
    print("This script meant to be importet rather than run directly.")