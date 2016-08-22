import random

rand_hand = [0,1,2] * 333
random.shuffle(rand_hand)

def show_me_the_hand(records):
    from random import choice
    import random
    now_turn = len(records)
    if now_turn <= 0:
        return choice(['gawi', 'bawi', 'bo'])
    son = ['gawi', 'bawi', 'bo']
    return son[rand_hand[now_turn-1]]
