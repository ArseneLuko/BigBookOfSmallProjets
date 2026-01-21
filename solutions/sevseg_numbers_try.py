# ' __ '
# '|__|'
# '|__|'

# s = {
# 'a': ['  ','__'],
# 'b': [' ','|'],
# 'c': [' ','|'],
# 'd': ['  ','__'],
# 'e': [' ','|'],
# 'f': [' ','|'],
# 'g': ['  ','__'],
# 'x': ' '
# }

# a = '__'
# b = '|'
# c = '|'
# d = '__'
# e = '|'
# f = '|'
# g = '__'
# x = ' '

# is_on = '__'
# is_off = '  '
# zero = []

# digits = {
#     '0': [
#     f'{s['x']}{s['a'][1]}{s['x']}',
#     f'{s['f'][1]}{s['g'][0]}{s['b'][1]}',
#     f'{s['e'][1]}{s['d'][1]}{s['c'][1]}'
#     ]
# }


   
# a_try = [
#     f'{x}{a}{x}',
#     f'{f}{g}{b}',
#     f'{e}{d}{c}'
# ]

open_digits = {
    '0': ['a', 'b', 'c', 'd', 'e', 'f'],
    '1': ['b', 'c'],
    '2': ['a', 'b', 'd', 'e', 'g'],
    '3': ['a', 'b', 'c', 'd', 'g'],
    '4': ['b', 'c', 'd', 'g'],
    '5': ['a', 'b', 'c', 'd', 'g'],
    '6': ['a', 'b', 'c', 'd', 'g'],
    '7': ['a', 'b', 'c', 'd', 'g'],
    '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    '9': ['a', 'b', 'c', 'd', 'g']
}

a = ''
b = ''
c = ''
d = ''
e = ''
f = ''
g = ''
x = ' '

segments_positions = [a, b, c, d, e, f, g, x]

all_segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x']

def get_state(segment, number):
    number = str(number)
    if segment in open_digits[number] and segment not in ('a','d','g'):
        return '|'
    elif segment in open_digits[number]:
        return '_'
    else:
        return ' '
    
rows = [3 * '']
wanted_number = 7

for seg in all_segments:
    for row in rows:
        row += get_state(seg, wanted_number)
    print(some)

print(segments_positions)


