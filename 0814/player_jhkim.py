import time

def show_me_the_hand(_):
    try:
        pick = int(str(time.time())[16])
        if (pick < 4):
            return 'bawi'
        if (pick < 7):
            return 'gawi'
        return 'bo'
    except Exception:
        return 'bawi'
