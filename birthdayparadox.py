"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math, simulation"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None
    
    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # return the matching birthday


# Display the intro:
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# Set up a tuple of month names in order:
MONTHS = ("Leden", "Únor", "Březen", "Duben", "Květen", "Červen",
          "Červenec", "Srpen", "Září", "Říjen", "Listopad", "Prosinec")

while True: # Keep asking until the user enters a valid amount.
    print("How many birthdays shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # user has entered a valid amount
print()

# generate and display the birthdays:
print(f"Vypisuji {numBDays} narozeninových dní:")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(", ", end="")
    monthName = MONTHS[birthday.month - 1]
    dateText = f"{birthday.day}. {monthName}"
    print(dateText, end="")
print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results
print("V této simulaci ", end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = f"{match.day}. {monthName}"
    print("má více lidí narozeniny ", dateText)
else:
    print("nemá nikdo narozeniny ve stejný den")
print()

# Run through 100 000 simulations
print(f"Generuji {numBDays} narozeninových dní 100 000 krát...")
input("Zmáčkni Enter pro zahájení simulací...")

print("Spouštím 100 000 dalších simulací")
simMatch = 0 # How many simulations had matching birthdays in them
for i in range(100_000):
    # report on the progress every 10_000 simulations:
    if i % 10_000 == 0: # alternatively if not i % 10_000:
        print(f"{i:_} simulací proběhlo")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print("100_000 simulací proběhlo")

# Display simulation result
probability = round(simMatch / 100_000 * 100, 2)
print(f"Ve 100_000 simulacích pro skupinu {numBDays} lidí,")
print(f"se vyskytlo společné datum narození {simMatch} krát.")
print(f"To znamená, že pro skupinu {numBDays} lidí je pravděpodobnost,")
print(f"že v ní budou dva lidé se stejným dnem narození {probability} %")
print("To je pravděpodobně více, než si si myslel*a")