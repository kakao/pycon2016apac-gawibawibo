from random import choice

draw_cnt = 1

def show_me_the_hand(records):
    global draw_cnt
    if len(records) == 0:
        return choice(['gawi', 'bawi', 'bo'])

    if (records[-1][1] == 0):
        draw_cnt += 1

    if (draw_cnt == 5):
        draw_cnt = 1
        br = records[-1][0]
        if br == 'gawi':
            return 'bawi'
        elif br == 'bowi':
            return 'bo'
        else:
            return 'gawi'
    else:
        return records[-1][0]
'''
r1 = []
r2 = []

for i in range(1000):
    h1 = show_me_the_hand(r2)
    h2 = show_me_the_hand(r1)

    if h1 == h2:
        print('match %d of 1000: tie' % i)
        r = 0
    elif (h1 == 'gawi' and h2=='bo') or (h1 == 'bawi' and h2 == 'gawi') or (h1 == 'bo' and h2 == 'bawi'):
        print('match %d of 1000: p1 win' % i)
        r = 1
    else:
        print('match %d of 1000: p2 win' % i)
        r = -1

    r1.append((h1, r))
    r2.append((h2, -r))
'''
