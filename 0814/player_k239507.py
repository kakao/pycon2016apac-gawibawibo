from math import sin, cos
import time

choices = ['gawi', 'bawi', 'bo']


def show_me_the_hand(records):
    factor_sin = round(abs(sin(time.time())))
    factor_cos = round(abs(cos(time.time())))
    return choices[int(factor_sin + factor_cos)]
