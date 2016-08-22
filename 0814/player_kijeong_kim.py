# coding: utf-8
# author: kijeong


dic_hands_indexed = {'gawi':0, 'bawi':1, 'bo':2}
lst_hands = ['gawi', 'bawi', 'bo']

def get_dic_hands_count(lst_counter_records):
    from collections import Counter
    count = Counter([x[0] for x in lst_counter_records])
    for k in range(3):
        if lst_hands[k] not in count.keys():
            count[lst_hands[k]] = 0
    return count


def check_if_same_hand(dic_hands_count):
    cnt_zero = 0
    for k in range(3):
        if dic_hands_count[lst_hands[k]] == 0:
            cnt_zero += 1
    return cnt_zero == 2


def get_better_hand_rand(lst_counter_records):
    cnt_last = 2
    if len(lst_counter_records) < cnt_last:
        return lst_counter_records[-1][0]
    count = get_dic_hands_count(lst_counter_records[-cnt_last:])
    lst_sorted = sorted(count, key=lambda x: count[x])
    idx = dic_hands_indexed[lst_sorted[0]]
    return lst_hands[(idx + 1) % 3]


is_same_hand = False
better_hand = lst_hands[0]


def get_better_hand_same(result_last):
    if result_last == -1:
        return better_hand
    elif result_last == 0:
        return lst_hands[(dic_hands_indexed[better_hand] + 1) % 3]
    elif result_last == 1:
        return lst_hands[(dic_hands_indexed[better_hand] + 2) % 3]
    else:
        return lst_hands[0]


def show_me_the_hand(records):
    global is_same_hand
    global better_hand

    lst_counter_records = records
    if len(lst_counter_records) < 10:
        return lst_hands[0]


    if len(lst_counter_records) % 10 == 0:
        is_same_hand = check_if_same_hand(get_dic_hands_count(lst_counter_records))
        better_hand = get_better_hand_same(lst_counter_records[-1][1])

    if is_same_hand:
        return better_hand
    else:
        return get_better_hand_rand(lst_counter_records)

