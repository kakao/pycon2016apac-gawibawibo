#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice


def show_me_the_hand(records):
    hand_cnt = [0, 0, 0]

    # 최초 60번은 랜덤
    if len(records) < 60:
        return choice(['gawi', 'bawi', 'bo'])

    # 이후에는 상대방이 낸 것을 평균내어 계산 후 리턴
    for hand in records:
        if hand is 'gawi':
            hand_cnt[0] += 1
        elif hand is 'bawi':
            hand_cnt[1] += 1
        elif hand is 'bo':
            hand_cnt[2] += 1

    ret = choice(['gawi', 'bawi', 'bo'])
    min = 999999
    min_idx = 0
    for idx in range(len(hand_cnt) - 1):
        if hand_cnt[idx] < min:
            min = hand_cnt[idx]
            min_idx = idx

    if min_idx == 0:
        return choice(['gawi', 'bawi'])
    elif min_idx == 1:
        return choice(['bawi', 'bo'])
    elif min_idx == 2:
        return choice(['gawi', 'bo'])
