hands = ['gawi', 'bawi', 'bo', 'bawi']
my_hand = 0

def show_me_the_hand(records):
    my_hand = (my_hand + 1) % 4
    return hands[my_hand]