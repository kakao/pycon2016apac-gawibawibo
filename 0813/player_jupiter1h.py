from random import choice

def show_me_the_hand(records):
    result=['gawi','bawi','bo']

    if len(records) == 0:
            return 'bo'
    else :
            return choice(result[0],result[1],result[2],result[2])
