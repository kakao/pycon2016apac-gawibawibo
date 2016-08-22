def show_me_the_hand(r):
    if len(r)==0:
        return 'bawi'
    elif r[0][0] =='bawi':
        return 'bawi'
    elif r[0][0] == 'bo':
        return 'bo'
    else:
        return 'bawi'
