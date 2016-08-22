from collections import Counter
selections = ['gawi', 'bawi', 'bo']
win = {'gawi':'bawi', 'bawi':'bo', 'bo':'gawi'}


def show_me_the_hand(records):
    if len(records) < 100:
        i = len(records) % 3
        return selections[i]
    elif len(records) < 200:
        c = Counter([s for s, r in records])
        m = c.most_common(1)[0]
        return win[m[0]]
    if sum([w for r, w in records[:100]]) < 5:
        winning = True
    else:
        winning = False
    if winning:
        c = Counter([record[0] for record in records])
        m = c.most_common(1)[0]
        return win[m[0]]
    else:
        i = len(records) % 3
        return selections[i]