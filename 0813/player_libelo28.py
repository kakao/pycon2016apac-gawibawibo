from random import choice
from collections import Counter
win = {'gawi':'bawi', 'bawi':'bo', 'bo':'gawi'}

def show_me_the_hand(records):
    if len(records) <= 200:
        return choice(['gawi', 'bawi', 'bo'])
    if 200 < len(records) < 300:
        c = Counter([record[0] for record in records])
        m = c.most_common(1)[0]
        return win[m[0]]
    if sum([w for r, w in records[:100]]) > 10:
        winning = True
    else:
        winning = False
    if winning:
        c = Counter([record[0] for record in records])
        m = c.most_common(1)[0]
        print(m)
        return win[m[0]]
    else:
        return choice(['gawi', 'bawi', 'bo'])