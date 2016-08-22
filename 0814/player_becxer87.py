def mersenne_twister():
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

def show_me_the_hand(records):
    choice = mersenne_twister() % 3
    now_turn = len(records)
    if now_turn <= 50:
        return ['gawi', 'bawi', 'bo'][choice]
    
    hist = [0,0,0]
    for rec in records:
        if (rec[0] == 'gawi'):
            hist[0] += 1
        elif (rec[0] == 'bawi'):
            hist[1] += 1
        else :
            hist[2] += 1

    target = mersenne_twister() % now_turn + 1
    if ( target <= hist[0] ):
        return 'bawi'
    elif (target <= hist[0] + hist[1]):
        return 'bo'
    else :
        return 'gawi'
