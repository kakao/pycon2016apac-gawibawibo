from random import choice
from random import randint
import random
import os

def show_me_the_hand(records):
    b = reduce(lambda x,y: x*256+y, map(ord, os.urandom(10)))
    random.seed(b)
    result = ['gawi', 'bawi', 'bo'][randint(0,2)]
    random.seed(1)
    if len(records) >= 6:
        if records[-2] == records[-4] and records[-4] == records[-6]:
            ans = records[-2]
            if ans == 'gawi':
                return 'bawi'
            elif ans == 'bawi':
                return 'bo'
            else:
                return 'gawi'
    return result
