# -*- coding: utf-8 -*-
import timeit
import operator

counter_attack_of = {
    'gawi': 'bawi',
    'bawi': 'bo',
    'bo': 'gawi',
}
results = ['gawi', 'bawi', 'bo']

def show_me_the_hand(records):
    win_count_of = {'gawi': 0, 'bawi': 0, 'bo': 0}
    for game in records:
        win_count_of[game[0]] += game[1]
    if min(win_count_of.items(), key=operator.itemgetter(1))[1] == 0:
        return results[int(timeit.timeit()*100000 % 3)]
    result = counter_attack_of[min(win_count_of.items(),
                                 key=operator.itemgetter(1))[0]]
    return result
