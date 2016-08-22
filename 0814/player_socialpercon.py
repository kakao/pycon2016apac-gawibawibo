hands = ['gawi', 'bawi', 'bo']
my_hand = ''

def show_me_the_hand(records):
    global my_hand
    (h1, r) = records
    if r == 1:
        for hand in hands:
            if h1 == hand:
                continue
            my_hand = hand
    elif r == 0:
        pass
    else:
        my_hand = h1

    return my_hand
