def show_me_the_hand(records):
    if len(records) == 0:
        return 'bo'

    if records[-1][1] == 0:
        if len(records) >= 3:
            if records[-1][0] + records[-2][0] + records[-3][0] == 2:
                if records[-1][0] == 'gawi':
                    return 'bawi'
                elif records[-1][0] == 'bo':
                    return 'gawi'
                elif records[-1][0] == 'bawi':
                    return 'bo'
            else:
                return records[-1][0]

    if records[-1][1] == 1:
        if records[-1][0] == 'gawi':
            return 'bawi'
        elif records[-1][0] == 'bo':
            return 'gawi'
        elif records[-1][0] == 'bawi':
            return 'bo'

    return 'gawi'
