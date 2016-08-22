def win_lose_ratio(hand_type, r):
    count = 0
    for i in r:
        if i[0] == hand_type:
            count = count + i[1]

    return count



hands = ['bawi', 'bo', 'gawi']
my_hand = 0

def show_me_the_hand(r):
    gawi_count = win_lose_ratio('gawi', r)
    bawi_count = win_lose_ratio('bawi', r)
    bo_count = win_lose_ratio('bo', r)

    if gawi_count > bawi_count and gawi_count > bo_count:
        return 'bawi'
    elif bawi_count > gawi_count and bawi_count > bo_count:
        return 'bo'
    elif bo_count > gawi_count and bo_count > bawi_count:
        return 'gawi'
    else:
        global my_hand
        my_hand = (my_hand + 1) % 3
        return hands[my_hand]
