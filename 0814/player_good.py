def show_me_the_hand(records):
    if len(records) == 0:
        return 'bawi'

    u = records[0][0]

    if u == 'bawi':
        return 'bo'

    if u == 'bo':
        return 'gawi'

    if u == 'gawi':
        return 'bawi'

    return 'bo'
