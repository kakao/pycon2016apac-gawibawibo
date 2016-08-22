import time
def show_me_the_hand(records=None):
    h = {0 : 'bawi', 1 : 'gawi', 2 : 'bo'}
    t = int(time.time()*(10**6))
    t = [int(i) for i in str(t)]
    t = sum(t)%3
    return h[t]
