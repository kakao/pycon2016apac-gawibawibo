import operator


def show_me_the_hand(records):
    my_records = []

    if len(records) == 0:
        return "bo"

    for each in records:
        my_records.insert(0, judge(each))

    mini = {}
    cnt = 0
    for each in my_records:
        cnt += 1
        if each in mini:
            mini[each] = (mini[each] + 1)
        else:
            mini[each] = 1

        if cnt > 20:
            my_records.pop()

    sorted_mini = sorted(mini.items(), key=operator.itemgetter(1))
    return sorted_mini[0][0]


def judge(one):
    if one[1] == 1:
        return 'bo' if one[0] == 'gawi' else ('gawi' if one[0] == 'bawi' else 'bawi')
    elif one[1] == 0:
        return one[0]
    else:
        return 'bo' if one[0] == 'bawi' else ('gawi' if one[0] == 'bo' else 'bawi')