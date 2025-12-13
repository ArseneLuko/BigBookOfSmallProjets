"""
String for a Cho-Han game in chohan_mine.py file. 
When adding a new string, add it first to an empty dictionary 'messages_empty', so it is prepared for adding new language

Maximum lenght of an item in dictionary is 78.
"""

# empty dictionary with all keys to use as a template
messages_empty = {
    "welcome": "",
    "separator": "",
    "enter_name": "",
    "enter_money": "",
    "not_decimal": "",
    "bet_and_purse": "",
    "not_a_number": "",
    "not_enough": "",
    "bet_accepted": ""
}

messages_en = {
    "welcome": "Welcome to play Cho-Han, a traditional Japanese gambling game using dice.",
    "separator": 78 * "-",
    "enter_name": "Enter your name: ",
    "enter_money": "Enter the amount you will be starting with. (an empty line = 5,000)",
    "not_decimal": "Please enter a number.",
    "bet_and_purse": "In your purse: {}, how much do you want to bet?",
    "not_a_number": "Please enter a number.",
    "not_enough": "You don't have enough money to bet so. You have: {}",
    "bet_accepted": "You've bet {}. Let's play"
}

