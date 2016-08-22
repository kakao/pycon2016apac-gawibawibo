from collections import Counter


def show_me_the_hand(records):
    c = Counter([x[0] for x in records])
    r = sorted(c, reverse=True)
    if not r:
        return 'bawi'
    else:
        if r[0] == 'gawi':
            return 'bawi'
        elif r[0] == 'bawi':
            return 'bo'
        else:
            return 'gawi'
