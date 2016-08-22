from random import choice

def show_me_the_hand(records):
    if len(records) == 0:
        return choice(['gawi', 'bawi', 'bo'])

    return choice((records[-1][0], choice(['gawi', 'bawi', 'bo'])))