from random import choice


def show_me_the_hand(records):
    if len(records) == 0:
        return choice(['gawi', 'bawi', 'bo'])
    return records[0][0]
