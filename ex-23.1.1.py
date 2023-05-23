from math import exp, log, sqrt
import os
import subprocess
import sys


def express(x, y):
    z = 3*(x**2) + sqrt(x**2 + y**2) + exp(log(x))
    return z

try:
    x = float(input('Enter x = '))
    y = float(input('Enter y = '))

    if x <= 0:
        print('x is not a positive number!')
        print('Tips: Please input a positive number for x and any number for y')
        print('Restarting the program...')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        exit()
    else:
        print('Result of expression =', express(x, y))

# except ValueError as error:
#     print('ERROR:', error)
#     print('Tips: Please input a positive number for x and any number for y')
#     print('Restarting the program...')
#     subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
#     exit()
    
except ValueError:
    print('ERROR: Value cannot be converted to a float number')
    print('Tips: Please enter number value')
    print('Restarting the program...')
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    exit()