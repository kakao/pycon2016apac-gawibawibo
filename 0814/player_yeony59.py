lose_hand = {'gawi': 'bo', 'bawi': 'gawi', 'bo': 'bawi'}
win_hand = {'gawi': 'bawi', 'bawi': 'bo', 'bo': 'gawi'}


def show_me_the_hand(records):
    if len(records) == 0:
        return 'bo'

    if records[-1][1] == 0:
        return lose_hand[records[-1][0]]

    return win_hand[records[-1][0]]