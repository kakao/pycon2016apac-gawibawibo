hands = ['gawi', 'bawi', 'bo']
i = 0
def show_me_the_hand(records):
    i += 1
    if i % 6 == 0:
        return hands[1]
    elif i % 3 == 0:
        return hands[2]
    return hands[0]

