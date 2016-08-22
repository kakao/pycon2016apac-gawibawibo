from random import choice

def show_me_the_hand(records):
    hand_set = {
        'gawi': 0,
        'bawi': 0,
        'bo': 0
    }

    if len(records) == 0:
        return choice(['gawi', 'bawi', 'bo'])
    else:
        for record in records:
            hand_set[record[0]] += record[1]

        max_val = max(hand_set.values())
        hand_choices = []

        for hand_key, hand_val in hand_set.items():
            if hand_val == max_val:
                hand_choices.append(hand_key)

        return choice(hand_choices)

