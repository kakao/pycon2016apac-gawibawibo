def show_me_the_hand(records):
    if len(records) % 5 == 0:
        return 'bawi'
    elif len(records) % 7 == 0:
        return 'gawi'
    else:
        return 'bo'
            
