def show_me_the_hand(records):
    if len(records)/2%4 == 0.0:
        return 'gawi'
    elif (len(records)/2%4 == 1.0): 
        return 'bawi'
    else:
        return 'bo'
