# syshin0316@gmail.com


import time


choices = ['gawi', 'bawi', 'bo']

def show_me_the_hand(records):
    return choices[int(time.time()) % 3]
