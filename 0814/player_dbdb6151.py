def show_me_the_hand(records):
    hands = ['gawi', 'bawi', 'bo']

    opponent_last_two = [
        records[0][0],
        records[1][0]
    ]
    for opponent_hand in opponent_last_two:
        hands.remove(opponent_hand)
    return hands[0]