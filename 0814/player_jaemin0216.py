hands = ['gawi', 'bawi', 'bo']
def show_me_the_hand(records):
    if len(records) == 0:
        return hands[0]

    return hands[records[0][1] + 1]
