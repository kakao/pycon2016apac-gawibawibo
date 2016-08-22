import time


def show_me_the_hand(_):
    return ['gawi', 'bawi', 'bo'][(int(time.time()*1000000)+2)%3]
