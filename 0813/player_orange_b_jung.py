from random import choice

HANDS = ['gawi', 'bawi', 'bo']

def show_me_the_hand(records):
    # list of the appearence of each hand
    your_hands_record = [records.count(hand) for hand in HANDS]

    if len(set(your_hands_record)) == 1: # if the apperence counts of the each hand are equal
        # random
        hand_to_return = choice(HANDS)
    else:
        # the hand that wins the opponent's hand which appears the most
        hand_to_return = HANDS[(your_hands_record.index(max(your_hands_record)) + 1) % 3]

    return hand_to_return

if __name__ == "__main__":
    print (show_me_the_hand(['bo', 'gawi', 'bawi', 'bawi']))
    print (show_me_the_hand(['bo', 'gawi', 'bawi']))
    print (show_me_the_hand(['bo']))
    print (show_me_the_hand([]))
