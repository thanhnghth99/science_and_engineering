import os
import subprocess
import sys
import numpy as np


def rad_deg():
    try:
        rad = float(input('Enter an angle in radian = '))
        if abs(rad) >= 0 and abs(rad) <= 2*np.pi:
            deg = rad * 180/np.pi
            print(rad, 'radian =', deg, 'degree')
            return deg
        else:
            raise ValueError('Invalid radian value for converting function! Try again...')
    except Exception as error:
        print('ERROR:', error)
        print('Restarting...!')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        exit()

def deg_rad():
    try:
        deg = float(input('Enter an angle in degree = '))
        if abs(deg) >= 0 and abs(deg) <= 360:
            rad = deg * np.pi/180
            print(deg, 'degree =', rad, 'radian')
            return rad
        else:
            raise ValueError('Invalid degree value for converting function! Try again...')
    except Exception as error:
        print('ERROR:', error)
        print('Restarting...!')
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        exit()

rad_deg()
deg_rad()