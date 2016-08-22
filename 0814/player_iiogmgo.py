import time

def show_me_the_hand(records):
    now = time.time()
    select_hand = int(now%5)

    if select_hand < 2:
        return 'gawi'
    elif select_hand < 3:
        return 'bawi'
    return 'bo'
