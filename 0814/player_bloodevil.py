import time

def show_me_the_hand(records):
    n = int(time.time()*100000)
    result = ['bawi', 'gawi', 'bo']
    return result[n%3]
