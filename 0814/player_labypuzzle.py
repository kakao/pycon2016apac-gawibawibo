import time

def choice():
    hand = ['gawi', 'bawi', 'bo']
    return hand[ (int(time.time()) % 1829) % 3]

def count(records):
    l = [r[0] for r in records]
    return [l.count('gawi'), l.count('bawi'), l.count('bo')]

def show_me_the_hand(records):
    if len(records) < 10:
        return choice()

    c = count(records)

    if c[0] > len(records) * 0.8:
        return 'bawi'
    if c[1] > len(records) * 0.8:
        return 'bo'
    if c[2] > len(records) * 0.8:
        return 'gawi'

    return choice()

print show_me_the_hand([('gawi', 0)] * 100)
