gbb = ['gawi', 'bawi', 'bo']

def show_me_the_hand(records):
    while len(records) > 0:
        p = records.pop()
        r = records.pop()
        if r == 'gawi':
            gbb.append('bawi')
        elif r == 'bawi':
            gbb.append('bo')
        else:
            gbb.append('gawi')
    gawi_n, bawi_n, bo_n = gbb.count('gawi'), gbb.count('bawi'), gbb.count('bo')

    ret_n = gawi_n
    ret = 'gawi'
    if ret_n < bawi_n:
        ret = 'bawi'
        ret_n = bawi_n
    if ret_n < bo_n:
        ret = 'bo'
    return ret
