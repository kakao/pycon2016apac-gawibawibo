def show_me_the_hand(records):
    recLen = len(records)
    if recLen == 0 or recLen ==1:
        return 'bo'
    if records[recLen-1][0] == records[recLen-2][0]:
        if records[recLen-1][0] == 'bawi':
            return 'bo'
        elif records[recLen-1][0] == 'gawi':
            return 'bawi'
        else:
            return 'gawi'

    return 'bo'
