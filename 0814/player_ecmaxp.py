K_CONST = 128
GAWI, BAWI, BO = "gawi", "bawi", "bo"
ALL = GAWI, BAWI, BO
WIN_TABLE = {GAWI: BAWI, BAWI: BO, BO: GAWI}
LOSE_TABLE = {BAWI: GAWI, BO: BAWI, GAWI: BO}

def show_me_the_hand(records):
    less = dict.fromkeys(ALL, 0)
    k = len(records)
    for t, (x, y) in enumerate(records[:K_CONST]):
        target = None
        if y == 1: target = LOSE_TABLE.get(x)
        elif y == -1: target = WIN_TABLE.get(x)
        if not target: target = ALL[(k + t) % 3]
        less[target] += 1

    return WIN_TABLE[sorted((v, k) for k, v in less.items())[-1][1]]
