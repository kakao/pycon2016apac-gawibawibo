import random

gbb = ['gawi', 'bawi', 'bo']

def show_me_the_hand(records):
    while len(records) > 0:
        r = records.pop()
        p = records.pop()
        if r == 'gawi':
            gbb.append('bawi')
        elif r == 'bawi':
            gbb.append('bo')
        else:
            gbb.append('gawi')
    return random.choice(gbb)
