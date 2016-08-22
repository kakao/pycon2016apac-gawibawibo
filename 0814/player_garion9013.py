#!/usr/local/bin/python3

from itertools import product
import time

# Poorly reconstructed random choice
def choice(arr):
    return arr[int(time.time()*10000000000000/13*7)%3]

wining_dict = {"bawi":"bo", "gawi":"bawi", "bo":"gawi"}
option = ["gawi", "bawi", "bo"]

# Param for initial fake
fake_pattern= ["bawi","gawi","gawi","gawi","gawi","gawi","gawi","bo","gawi","bawi"]
fake_period = len(fake_pattern)

# Param for frequency training
len_seq = 5
train_period = 3 ** len_seq
seq = list(product(option, repeat=len_seq))
freq_dict = {}
freq_thresh = 10

# Param for repetitive pattern
repetition_score = 0
repetition_thresh = len_seq

# Param for shadowing pattern
shadowing_detect_window = 7
my_history = ["" for i in range(shadowing_detect_window)]

def q_pop(my_history):
    my_history[:]=my_history[1:]

def q_push(my_history, val):
    my_history.append(val)

def show_me_the_hand(records):
    global repetition_score
    global seq
    global freq_dict
    global fake_pattern
    global my_history

    # Baseline policy: poor random
    res = choice(option) 

    if len(records) < fake_period:
        # Fake patterns for initial
        return fake_pattern.pop()
    elif len(records) < (fake_period + train_period):
        # See probability patterns and train it
        history = tuple([row[0] for row in records[-len_seq:]])

        if history in freq_dict.keys():
            freq_dict[history] += 1
        else:
            freq_dict[history] = 0

        return res
    else:
        # Repetitive pattern: shadowing
        if records[-1][0] == records[-2][0]:
            repetition_score += 1
            if repetition_score > repetition_thresh:
                res = wining_dict[records[-1][0]]

        # High frequency pattern: predict & action
        window = len_seq - 1
        history_sample = tuple([row[0] for row in records[-window:]])

        candidate = {}
        for elem in freq_dict.keys():
            if history_sample == elem[:-1]:
                candidate[elem] = freq_dict[elem]
        if candidate != {}:
            if freq_dict[max(candidate)] > freq_thresh:
                res = wining_dict[max(candidate)[-1]]

        # Shadowing pattern
        shadowing_hit = False
        history_sample = tuple([row[0] for row in records[-len(my_history):]])
        for i in range(len(my_history)):
            if my_history[:-i] == list(history_sample[i:]):
                shadowing_hit = i
                break;

        if shadowing_hit != False:
            res = wining_dict[my_history[-shadowing_hit]]

        q_pop(my_history)
        q_push(my_history, res)

        return res
