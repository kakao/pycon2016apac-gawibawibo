# author : iljichoi@gmail.com
# rule summary
# 1. If the user definetly choose randomly, against it.
# 2. all of the record are same
# 3. two uniq item
# cannot find rule and length meets 50, then only return 'bo'
import random
from random import choice

rule_index = -1
against_seed = -1
items = ['gawi', 'bawi', 'bo']


def show_me_the_hand(records):
    # find random user
    global rule_index
    global items
    if len(records) == 50:
        # rule 2
        if search_same(records):
            rule_index = 2
        # rule 3
        elif search_two(records):
            rule_index = 3

        # rule 1
        against_seed = search_seed(records)
        if against_seed != -1:
            rule_index = 1

    if rule_index == -1:
        select_idx = len(records) // 100 % 3
        return items[select_idx]
    elif rule_index == 1:
        random.seed(against_seed)
        future_item = [choice(items) for _ in range(len(records) + 1)][-1]
        return choose_against(future_item)
    elif rule_index == 2:
        return choose_against(records[-1])
    elif rule_index == 3:
        return 'gawi'


def choose_against(record):
    if record == 'gawi':
        return 'bawi'
    elif record == 'bawi':
        return 'bo'
    else:
        return 'gawi'


def search_seed(records):
    global items
    for idx in range(100000 + 1):
        random.seed(idx)
        temp = [choice(items) for _ in range(len(records))]
        if records == temp:
            return idx

    return -1


def search_same(records):
    set_of_records = set(records)
    if len(set_of_records) <= 1:
        return True
    else:
        return False


def search_two(records):
    set_of_records = set(records)
    if len(set_of_records) == 2:
        return True
    else:
        return False
