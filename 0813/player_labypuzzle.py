from random import choice

def show_me_the_hand(records):
    return choice(['gawi', 'bawi', 'bo']) if len(records) == 0 else records[0][0]