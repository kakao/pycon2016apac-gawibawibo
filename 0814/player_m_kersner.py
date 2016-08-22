#!/usr/bin/env python
# Martin Kersner, m.kersner@gmail.com

from time import time

def show_me_the_hand(records):
    global last_move
    options =  ['gawi', 'bawi', 'bo']

    if len(records) == 0:
        last_move = options[0]
        return last_move

    last_idx = len(records)-1

    if records[last_idx][1] == -1:
        last_move = options[options.index(records[last_idx][0])]
        return last_move
    elif records[last_idx][1] == 1:
        return last_move
    else:
        last_move = options[(options.index(records[last_idx][0]) + 1) % 3]
        return last_move
