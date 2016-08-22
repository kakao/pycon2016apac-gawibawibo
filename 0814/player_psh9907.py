hands = ['gawi', 'bawi', 'bo']


def show_me_the_hand(records):
    l = len(records)
    if l == 0:
        return hands[0]
    elif records[l - 1][0] == 'gawi':
        return hands[2]
    elif records[l - 1][0] == 'bawi':
        return hands[0]
    elif records[l - 1][0] == 'bo':
        return hands[1]
