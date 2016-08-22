def show_me_the_hand(records):
    if len(records) == 0:
        return 'bo'
    else:
        temp = records[int(len(records)/2-1)*2]
        if temp == 'gawi':
            return 'bawi'
        elif temp == 'bawi':
            return 'bo'
        elif temp == 'bo':
            return 'gawi'
