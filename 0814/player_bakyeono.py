# programmed by Bak Yeon O (bakyeono@gmail.com)

def show_me_the_hand(records):
    try:
        # let's see how my opponent moves for 4 times...
        if len(records) < 5:
            return 'bo'

        # predict my opponent's next move...
        recent_records = records[-24:]
        frequencies = {
            'gawi': 0,
            'bawi': 0,
            'bo': 0,
        }
        for hand, result in recent_records:
            if hand == 'gawi' or hand == 'bawi' or hand == 'bo':
                frequencies[hand] += 1
        predictions = sorted(frequencies, key=frequencies.get, reverse=True)

        # i'll win this
        if predictions[0] == 'gawi':
            return 'bawi'
        if predictions[0] == 'bawi':
            return 'bo'
        if predictions[0] == 'bo':
            return 'gawi'

        # if something goes wrong, stick with bawi
        return 'bawi'

    # if something goes wrong, stick with bawi
    except Exception:
        return 'bawi'
