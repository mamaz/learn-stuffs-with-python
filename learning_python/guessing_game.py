"""guesing game
to show using exception to catch not int input
"""
import random

try:
    found = False
    random_num = random.randint(1,10)
    while not found:
        num = int(input('input your guess from 1 to 20: '))

        if num < random_num:
            print('pick higher number')
        elif num > random_num:
            print('pick lower num')
        else:
            print('Yay, you found the number')
            found = True

except Exception as e:
    print(f'Error: your input is not an int', e)
