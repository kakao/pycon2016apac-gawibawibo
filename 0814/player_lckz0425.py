from random import choice

def show_me_the_hand(records):
    if len(records) == 0:
        return 'gawi'

    if records[0][0] == 'gawi':
        return 'bawi'
    elif records[0][0] == 'bawi':
        return 'bo'
    else:
        return 'bawi'
   # print(records)
    return 'bawi'
