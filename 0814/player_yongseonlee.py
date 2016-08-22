def show_me_the_hand(records):
    def get_opposite_hand(hand, win):
        return hands[(hands.index(hand)-win)%3]

    hands = ['gawi', 'bawi', 'bo']
    if len(records) < 3:
        return hands[len(records)]

    result = {}
    for hand in hands:
        result[hand] = 0

    records = records[:200]
    my_last_hand = get_opposite_hand(*records[0])

    for i in range(1, len(records)):
        my_hand = get_opposite_hand(*records[i])
        if my_hand == my_last_hand:
            result[records[i-1][0]] += 1

    sorted_result = list(result.items())
    sorted_result.sort(key=lambda x: x[1])
    return get_opposite_hand(sorted_result[-1][0], -1)
