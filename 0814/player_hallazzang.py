import time

def show_me_the_hand(records):
    return ('gawi', 'bawi', 'bo')[int(time.clock() * 99990) % 3]