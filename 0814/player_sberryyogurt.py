def max_gawi_bawi_bo(gawi, bawi, bo):
    res = max(gawi, bawi, bo)
    if res == gawi:
        return 'bawi'
    elif res == bawi:
        return 'bo'
    else:
        return 'gawi'

def show_me_the_hand(records):
    gawi = 0
    bawi = 0
    bo = 0

    for r in records:
        if r[0] == 'gawi':
            gawi += r[1]
        elif r[0] == 'bawi':
            bawi += r[1]
        else:
            bo += r[1]

    return max_gawi_bawi_bo(gawi, bawi, bo)
