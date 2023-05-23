import os
import subprocess
import sys


def fibonacci(n):
    try:
        if n < 0:
            raise ValueError('Invalid input number!')
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except Exception as error:
        print('ERROR:', error)
        print('Tips: Please enter input that greater than or equal to 0')
        print('Restarting the program...')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        exit()

n = int(input('Enter non-negative number n = '))
print(n, 'first Fibonacci numbers =', fibonacci(n))