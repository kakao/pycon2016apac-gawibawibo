# mersenne twister start ------------------------------------------------
# code from: http://code.activestate.com/recipes/578056-mersenne-twister/
from datetime import datetime

mt_list = [0 for i in range(624)]
mt_idx = 0
bm_1 = (2 ** 32) - 1
bm_2 = 2 ** 31
bm_3 = (2 ** 31) - 1

now_time = datetime.now()
mt_list[0] = now_time.microsecond
for i in range(1, 624):
    mt_list[i] = ((1812433253 * mt_list[i-1]) ^ \
            ((mt_list[i-1] >> 30) + i)) & bm_1

def mersenne_twister():
    global mt_idx
    global mt_list
    if mt_idx == 0:
        for i in range(624):
            tmp1 = (mt_list[i] & bm_2) + (mt_list[(i+1) % 624] & bm_3)
            mt_list[i] = mt_list[(i+397) % 624] ^ (tmp1 >> 1)
            if tmp1 % 2 != 0:
                mt_list[i] ^= 2567483615
    tmp2 = mt_list[mt_idx]
    tmp2 ^= tmp2 >> 11
    tmp2 ^= tmp2 >> 11
    tmp2 ^= (tmp2 << 7) & 2636928640
    tmp2 ^= (tmp2 << 15) & 4022730752
    tmp2 ^= tmp2 >> 18
    mt_idx = (mt_idx+1) % 624
    return tmp2
# mersenne twister end --------------------------------------------------

rand_hand = [0,1,2] * 33333

def show_me_the_hand(records):
    global rand_hand
    hand_set = ['gawi', 'bawi', 'bo']
    now_turn = len(records)
    if now_turn <= 0:
        return hand_set[mersenne_twister() % 3]
    return hand_set[rand_hand.pop(mersenne_twister() % len(rand_hand))]
