def min_max_ratio(records):
    li = [a for (a, i) in records]
    ratio = {'gawi': 0, 'bawi': 0, 'bo': 0}

    for a in li:
        ratio[a] += 1

    if ratio['gawi'] == ratio['bawi'] == ratio['bo']:
        return 0, 0, None, None

    for k in ratio.keys():
        ratio[k] /= len(li)
        # print('ratio[%s]=%.1f' % (k, ratio[k]))

    min_ratio, max_ratio, min_enemy, max_enemy = 1.0, 0.0, None, None
    for k in ratio.keys():
        if ratio[k] > max_ratio:
            max_ratio, max_enemy = ratio[k], k
        if ratio[k] < min_ratio:
            min_ratio, min_enemy = ratio[k], k
    return min_ratio, max_ratio, min_enemy, max_enemy


def check_pattern(records):
    li = [a for (a, i) in records]
    for step in range((len(li) // 2), 0, -1):
        li1, li2 = li[:step], li[step:step * 2]
        if li1 == li2:
            return li[step - 1]


def show_me_the_hand(records):
    my_hand_from_enemy = {
        'gawi': 'bawi',
        'bawi': 'bo',
        'bo': 'gawi'
    }

    try:
        if len(records) == 0:
            return 'bawi'
        elif len(records) == 1:
            return 'bo'
        # elif len(records) == 2:
        #     return 'gawi'
        else:
            enemy_by_pattern = check_pattern(records)
            if enemy_by_pattern:  # 상대방의 패턴을 읽어서, 대응해보자.
                # print('by pattern -> ', my_hand_from_enemy[enemy_by_pattern])
                return my_hand_from_enemy[enemy_by_pattern]
            else:  # 패턴이 없다면..
                min_ratio, max_ratio, min_enemy, max_enemy = min_max_ratio(records)
                if max_enemy and max_ratio > 0.36:  # 많이 내는 종류가 있다면, 다시 낼 확률이 높다.
                    # print('by enemy max -> ', my_hand_from_enemy[max_enemy])
                    return my_hand_from_enemy[max_enemy]
                else:  # 많이 내는 종류가 없다면, 안 낸 것을 낼 확률이 높다.
                    # print('by enemy min -> ', my_hand_from_enemy[min_enemy])
                    return my_hand_from_enemy[min_enemy]
    except:
        return 'gawi'
