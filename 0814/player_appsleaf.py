#!/bin/python3
import time

hands = ['gawi', 'bawi', 'bo']
r1 = []

def show_me_the_hand(records):
    my_hand = int(round(time.time() ))
    my_hand = (my_hand + 1) % 3
    return hands[my_hand]
