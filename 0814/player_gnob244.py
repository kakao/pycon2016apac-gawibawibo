hands = ['gawi', 'bawi', 'bo']
my_hand = 0

def show_me_the_hand(records):
    statics = [0, 0, 0]

    for hand, res in records:
        statics[hands.index(hand)] += res

    result = list(zip(statics, hands))
    result.sort()
    
    rand = (id(result) + len(records)) % 100

    if rand < 40:
        my_hand = -1
    elif 40 <= rand and rand < 70:
        my_hand = 1
    else:
        my_hand = 0

    return result[my_hand][1]
