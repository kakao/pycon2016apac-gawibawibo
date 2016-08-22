def show_me_the_hand(records):
    mode = 0
    if len(records) % 3 == 0:
        mode = (mode + 1) % 3
    hand = ['gawi', 'bawi', 'bo']
    return hand[mode]
