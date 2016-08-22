n = 1

def show_me_the_hand(records):
    global n

    hand = ['gawi', 'bawi', 'bo']
    len_r = len(records)

    sel = (len_r * len_r + n) % 2
    if sel == 0:
        n = (len_r * len_r + n) % 10000
    elif sel == 1:
        n = (n * len_r * n) % 10000

    submit = hand[n % 3]

    return submit
