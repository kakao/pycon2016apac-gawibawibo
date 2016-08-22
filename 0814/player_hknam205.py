import time
now = time.localtime()
hands = ['gawi', 'bawi', 'bo']
my_hand = 0

def show_me_the_hand(records):
    my_hand = now.tm_sec%3
    return hands[my_hand]
