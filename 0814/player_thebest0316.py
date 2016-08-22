def show_me_the_hand(records):
    if len(records) == 0:
        return 'gawi'
    elif records[0][0] == 'gawi' :
        return 'bo'
    elif records[0][0] == 'bawi' :
        return 'gawi'
    return 'bawi'