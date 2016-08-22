import time

hands = ['gawi', 'bawi', 'bo']
my_hand = 0


def show_me_the_hand(records):

    #@@time.sleep(0.0000123523)
    my_hand = int(str(time.time())[-2:]) % 3
    return hands[my_hand]

