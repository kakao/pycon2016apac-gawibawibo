#-*- coding: utf-8 -*-
hands = ['gawi', 'bawi', 'bo']

seed = 1

def my_rand():
    global seed
    seed = (seed * 1103515245 + 12345) & 0x7fffffff;
    return seed;

def show_me_the_hand(records):
    if len(records) == 0:
        return 'bo'
    score = { hands[0] : 0 , hands[1] : 0 , hands[2] : 0 }
    total_score = 0
    record_cnt = len(records)
    tmp = 0;

    for idx in range(0,record_cnt):
        rec = records[idx]
        score[rec[0]] += rec[1]
        tt = (record_cnt-idx/2)
        tmp += tt
        total_score += rec[1] * tt
    total_score /= float(tmp)


    maxidx = 0
    maxval = 0
    for idx in range(0,3):
        hand = hands[idx]
        if maxval < score[hand]:
            maxval =  score[hand]
            maxidx = idx
    addval = 0
    whim = False
    if record_cnt > 20:
        if total_score > 0.0:
            whim = (my_rand() % 100) < (total_score*2000)
        else:
            whim = (my_rand() % 100) < 10

    if whim:
        addval = 1+ (my_rand() % 2)

    ret = hands[ (maxidx+1+addval) % 3]
    return ret


