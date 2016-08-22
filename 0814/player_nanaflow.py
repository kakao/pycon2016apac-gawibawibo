# -*- coding:utf-8 -*-
__author__ = 'BryanCho'


def show_me_the_hand(records):
    if not records or len(records) < 100:
        if len(records) % 3 == 0:
            return 'gawi'
        elif len(records) % 3 == 1:
            return 'bawi'
        else:
            return 'bo'
    else:
        return_rps = {"gawi": "bawi", "bawi": "bo", "bo": "gawi"}
        user_rps = records[-2]
        return return_rps[user_rps]