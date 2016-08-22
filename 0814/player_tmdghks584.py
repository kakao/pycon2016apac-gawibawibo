hands = ['bo', 'bawi', 'gawi']
my_hand = 0

def show_me_the_hand(records):
    my_hand = (my_hand + 1) % 3
    return hands[my_hand]
