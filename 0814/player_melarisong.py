import time, collections

lose_hands = ["gawi", "bawi", "bo"]
win_hands = ["bawi", "bo", "gawi"]


def win(lose):
    return lose_hands.index(lose)

def show_me_the_hand(records):
    data = collections.Counter(records)
    if len(data) :
        oppo, res = data.most_common()[0]
        hand = win_hands[win(oppo[0])]

    else: 
        hand = lose_hands[int(time.time() % 3)]
    
    return hand
