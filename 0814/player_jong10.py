#!/usr/bin/env python3
# coded by jong10

import time

num2str = ('gawi', 'bawi', 'bo')
str2num = dict((x, i) for i, x in enumerate(num2str)) 
strategy_index = 0
strategies = (min, max)


def get_strategy(records):
    global strategy_index 
    global strategies
    if is_defeat_continuously(5, records):
        strategy_index = (strategy_index + 1) % len(strategies)
        #print("switch -> %d" % strategy_index)
    return strategies[strategy_index]


def is_defeat_continuously(times, records):
    sum_value = sum(int(value) for which, value in records[-times:])
    #print("sum_value = %d, %s" % (sum_value, records[-times:]))
    return sum_value == -times


def get_stats(records):
    s = {}
    for which, state in records:
        s[which] = s.get(which, 0) + 1
    return s


def predict_enemy_next(records):
    strategy = get_strategy(records)
    enemy_stats = get_stats(records)
    enemy_next, count = strategy(enemy_stats.items(), key=lambda x: x[1])
    return enemy_next


def get_my_next(enemy_next):
    return num2str[(str2num[enemy_next] + 1) % len(num2str)]


def show_me_the_hand(records):
    if len(records) == 0:
        idx = (int(time.time() * (10 ** 20))) % 3
        return num2str[idx]
    enemy_next = predict_enemy_next(records)
    return get_my_next(enemy_next) 
