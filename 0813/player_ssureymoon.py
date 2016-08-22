from random import choice
from collections import defaultdict


def show_me_the_hand(records):

    hands = ['gawi', 'bawi', 'bo']

    if len(records) == 0:
        return choice(hands)

    # 현재까지 상대방이 가장 많이 낸 것을 찾기
    bias = defaultdict(int)
    bias[records[-1][0]] += 1
    most_bias_hand = max(bias, key=lambda k:bias[k])

    if most_bias_hand == 'gawi':
        return 'bawi'
    if most_bias_hand == 'bo':
        return 'gawi'
    return 'bo'



