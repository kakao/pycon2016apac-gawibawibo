hands = ['gawi', 'bawi', 'bo']
hands_index = {i: hand for hand, i in enumerate(hands)}


def show_me_the_hand(records):
    if len(records) == 0:
        return hands[1]  # bawi

    # if I won
    if records[0][1] == -1:
        return records[0][0]

    # or tied or lost
    else:
        my_hand = (hands_index[records[0][0]] + 1) % 3
        return hands[my_hand]

