def show_me_the_hand(records):
    if len(records) == 0:
        return 'bawi'
    gawi = 0
    bawi = 0
    bo = 0
    for record in records:
        if record[0] == 'gawi':
            gawi += record[1]
        elif record[0] == 'bawi':
            bawi += record[1]
        elif record[0] == 'bo':
            bo += record[1]

    max_hand = max([gawi, bawi, bo])

    if len(records) != 0 and max_hand == 0:
        my_hand = 'gawi'
    elif gawi == max_hand:
        my_hand = 'bawi'
    elif bawi == max_hand:
        my_hand = 'bo'
    else:
        my_hand = 'gawi'
    return my_hand
