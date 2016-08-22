import time
entry = ['gawi','bawi','bo']

def show_me_the_hand():
    global entry
    idx = time.localtime().tm_sec%len(entry)
    return entry[idx]