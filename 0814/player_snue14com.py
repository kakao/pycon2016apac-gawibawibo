def show_me_the_hand(records):
    if len(records) == 0:
        return 'gawi'
    elif records[-1][-1] == 1:
#        print('이겼소')
        return records[-1][0]
    elif records[-1][-1] == 0:
#        print('비겼소')
        if records[-1][0] == 'bawi':
            return 'bo'
        elif records[-1][0] == 'bo':
            return 'gawi'
        else:
            return 'bawi'
    elif records[-1][-1] == -1:
#        print('졌소')
        if records[-1][0] == 'bawi':
            return 'gawi'
        elif records[-1][0] == 'bo':
            return 'bawi'
        else:
            return 'bo'
