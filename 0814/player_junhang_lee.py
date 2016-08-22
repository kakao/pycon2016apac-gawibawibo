def show_me_the_hand(records):
    if len(records) < 100:
        return 'bawi'

    else:
        score = 0
        for weapon, res in records:
            score += res

        if score < 0:
            return 'bo'
        elif score > 0 and float(score) < float(len(records) * 0.1):
            return 'gawi'
        else:
            return 'bawi'

