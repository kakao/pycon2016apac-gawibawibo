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

# global var
lose_weight = 1000
algo_switch = 0 # 0: random, 1: most win, 2: win thing to p2's most hand
b_win_power = 0.0

# algo1: return most win thing
def algo1(records):
    rs_dict = {'gawi':0, 'bawi':0, 'bo':0}
    for record in records:
        if record[1] == -1:
            rs_dict[record[0]] = rs_dict[record[0]] + 1
    return max(rs_dict, key=lambda i: rs_dict[i])

# algo2: return win to be most hand thing:
def algo2(records):
    col1 = [row[0] for row in records]

    # 0: gawi 1: bawi 2: bo
    cnt_list = []
    cnt_list.append(col1.count('gawi'))
    cnt_list.append(col1.count('bawi'))
    cnt_list.append(col1.count('bo'))

    result = cnt_list.index(max(cnt_list))
    if result == 0:
        return 'bawi'
    elif result == 1:
        return 'bo'
    else:
        return 'gawi'

def change_algo(now_switch):
    '''
    new_switch = now_switch
    while new_switch == now_switch:
        new_switch = mersenne_twister() % 5
    return new_switch
    '''
    '''
    return (now_switch + (mersenne_twister() % 5)) % 5
    '''
    #'''
    return (now_switch + 2) % 5
    #'''

# show me the lion doll
def show_me_the_hand(records):
    global lose_weight
    global algo_switch
    global b_win_power

    r_set = ['gawi', 'bawi', 'bo']
    # phase1 means no pattern phase -> i will hand randomize(merssen_twister)
    phase1 = 100

    game_total = len(records)
    col2 = [row[1] for row in records] # 1, 0, -1
    cwin = col2.count(-1) # enemy -1(lose) => me win
    cdraw = col2.count(0) # enemy 0(draw) => me draw
    close = col2.count(1) # enemy 1(win) => me lose

    # hand in phase1
    if game_total < phase1:
        return r_set[mersenne_twister() % 3]
    # hand after phase1
    else:
        # win_power is my winning percent without draw count
        # total count = win count + lose count
        win_power = (float)(cwin) / (game_total - cdraw)
        # win_power decrease means my current algo is weaker than ohter
        if win_power < b_win_power:
            # increase lose weight
            lose_weight += 1
        b_win_power = win_power

        # lose weight is bigger than 3 => -9pts
        if lose_weight > 3:
            # change number of algorithm
            algo_switch = change_algo(algo_switch)
            lose_weight = 0

        # algo0 : randomize
        if algo_switch == 0:
            return r_set[mersenne_twister() % 3]
        # algo1 : many times to win thing
        elif algo_switch == 1:
            return algo1(records)
        # algo2: win to algo1
        elif algo_switch == 2:
            return r_set[(r_set.index(algo1(records)) + 1) % 3]
        # algo3 : many times to hand from other
        elif algo_switch == 3:
            return algo2(records)
        # algo4 : win to algo3
        elif algo_switch == 4:
            return r_set[(r_set.index(algo2(records)) + 1) % 3]
