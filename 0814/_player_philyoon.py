#!/usr/bin/env python3
# -*- coding: utf8

import time


def my_dice():
    #@@time.sleep(0.0003)
    n = int(str(time.time() * 1000)[-1])
    return n % 3


def show_me_hand(records):
    #@@time.sleep(0.0001)
    return ['gawi', 'bawi', 'bo'][my_dice()]


if __name__ == '__main__':
    for i in range(100):
        print(show_me_hand([]))
