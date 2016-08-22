#!/usr/bin/python3
# -*- coding: utf-8 -*-
## Author: LuHa(munhyunsu@gmail.com)

# Library import area
import random


def show_me_the_hand(records):
    hands = list()
    gawi_bawi_bo_list = ['gawi', 'bawi', 'bo']


    for hand in records:
        if(hand[0] is 'gawi'):
            hands.append('bawi')
        elif(hand[0] is 'bawi'):
            hands.append('bo')
        elif(hand[0] is 'bo'):
            hands.append('gawi')
        else:
            hands.append(random.choice(gawi_bawi_bo_list))

    if(len(hands) != 0):
        return random.choice(hands)
    else:
        return random.choice(gawi_bawi_bo_list)
