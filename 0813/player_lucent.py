from random import choice, random
from math import sqrt

def show_me_the_hand(_records):

    n = len(_records)
    if n == 0:
        return choice(['bawi', 'bo', 'gawi'])

    FULL_RANDOM = [1./3, 1./3, 1./3]
    trans = {'gawi': 0, 'bawi': 1, 'bo': 2, 1:1, 2:2, 0:0}
    itrans = {0:'bawi', 1:'bo', 2:'gawi'}
    records = [trans[x] for x in _records if x not in (1, 0, -1)]


    def create_simple_chain(h_width):
        assert(h_width == len(records[n-h_width:]))
        steps = len(records) - h_width
        table = {}
        for i in range(steps):
            t = tuple(records[i-h_width:i])
            if table.get(t) is None:
                table[t] = [0.,0.,0.]
            table[t][records[i]] += 1

        return table

    def get_dist(h, h_table):
        h = tuple(h)
        if h_table.get(h) is None:
            return FULL_RANDOM
        return h_table[h]

    n = len(records)

    tries = [2, 4, 8, 16, 32, 64]
    tbs = {}
    for x in tries:
        if x > n:
            break
        tbs[x] = create_simple_chain(x)

    def argmax(x):
        max_i = 0
        for i in range(3):
            if x[i] > x[max_i]:
                max_i = i
        return max_i

    cnt = [0, 0, 0]
    for x in tries:
        if x > n:
            break
        cnt[argmax(get_dist(records[n-x:], tbs[x]))] += 1

    if cnt[argmax(cnt)] > 2:
        return itrans[argmax(cnt)]

    return choice(['bawi', 'bo', 'gawi'])
