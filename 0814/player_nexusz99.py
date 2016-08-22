import time


def show_me_the_hand(records):
    c = ['gawi', 'bawi', 'bo']
    a = int(time.time()) % 3

    if len(records) == 0:
        return c[0]

    if len(records) >= 2:
        i = (c.index(records[1]) + 2) % 3

    if len(records) == 1:
        i = (c.index(records[0]) + 2) % 3

    return c[i]
