import time

GAWI = 'gawi'
BAWI = 'bawi'
BO = 'bo'

WIN = 1
TIE = 0
LOST = -1

HANDS = (GAWI, BAWI, BO)
RESULT_TYPES = (
            (GAWI, WIN),
            (GAWI, TIE),
            (GAWI, LOST),
            (BAWI, WIN),
            (BAWI, TIE),
            (BAWI, LOST),
            (BO, WIN),
            (BO, TIE),
            (BO, LOST)
            )

def get_any_hand():
    return (GAWI, BAWI, BO)[int(time.time() % 3)]

def second_st(records):
    if 2 > len(records):
        return get_any_hand()

    result_table = [[0 for y in range(len(HANDS))] for x in range(len(RESULT_TYPES))]
    for idx in range(0, len(records)-1, 2):
        r = records[idx]
        n_hand = records[idx + 1][0]
        result_table[RESULT_TYPES.index(r)][HANDS.index(n_hand)] += 1

    r = records[-1]
    value = max(result_table[RESULT_TYPES.index(r)])
    if 0 == value:
        return get_any_hand()
    else:
        return HANDS[(((result_table[RESULT_TYPES.index(r)].index(value)) + 1) % len(HANDS))]

HANDS_FOR_FIRST = [GAWI, BAWI, BO]
def first_st(records):
    global HANDS_FOR_FIRST
    if 0 == len(records):
        for i in range(int(time.time() % 3)):
            hand = HANDS_FOR_FIRST.pop(0)
            HANDS_FOR_FIRST.append(hand)
    hand = HANDS_FOR_FIRST.pop(0)
    HANDS_FOR_FIRST.append(hand)
    return hand

STRATEGIES = [first_st, second_st]
WINS = 0
GAMES = 0.0
def show_me_the_hand(records):
    global WINS
    global GAMES
    if 0 != len(records):
        WINS += 1 if -1 == records[-1][1] else 0
    GAMES += 1
    if 1 < len(STRATEGIES) and 50 < GAMES and 0.3 > (WINS/GAMES):
        STRATEGIES.pop(0)
        GAMES = 0

    return STRATEGIES[0](records)
