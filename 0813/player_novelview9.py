from random import choice

def show_me_the_hand(records):

    if len(records) == 0:
        return 'bo'
    elif records[-2][0] == 'gawi':
        return 'bawi'
    elif records[-2][0] == 'bawi':
        return 'bo'
    return 'gawi'
