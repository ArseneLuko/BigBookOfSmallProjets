import datetime
import random

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

def generate_bdays(group_size):
    birthdays = []
    first_day = datetime.date(2001, 1, 1)
    for i in range(group_size):
        birthdays.append(first_day + datetime.timedelta(random.randrange(365)))
    return birthdays

def input_group_size():
    while True:
        print('How many birthdays shall I generate? (max 100)')
        group_size = input('>')
        if group_size.isdecimal() and (1 < int(group_size) < 101):
            break
    return int(group_size)

def print_bdays(birthdays) -> None:
    for position, date in enumerate(birthdays):
        days = [MONTHS[date.month - 1] + str(date.day)]
    pass


if __name__ == "__main__":
    # birthdays = generate_bdays(input_group_size())
    birthdays = generate_bdays(3)
    print_bdays(birthdays)
    pass