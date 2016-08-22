from time import time


def babo_random(default=3):
    return int(time() % default)


def show_me_the_hand(records):
    gawibwibo = ['gawi', 'bawi', 'bo']

    if len(records) == 0:
        return gawibwibo[babo_random(3)]
    else:
        last_game_index = len(records) - 1
        try_last_game = records[last_game_index][0]
        result_last_game = records[last_game_index][1]
        try_index_last_game = gawibwibo.index(try_last_game)

        if (babo_random(10) + 1) % 3 == 0:
            return gawibwibo[babo_random(3)]
        else:
            if result_last_game == 0:
                temp = babo_random(3)
                del gawibwibo[temp]
                return gawibwibo[babo_random(2)]
            elif result_last_game == 1:
                strategy = babo_random(3)
                if strategy == 0:
                    return gawibwibo[babo_random(3)]
                elif strategy == 1:
                    temp = babo_random(3)
                    return gawibwibo[temp]
                else:
                    del gawibwibo[try_index_last_game]
                    return gawibwibo[babo_random(2)]
            elif result_last_game == -1:
                strategy = babo_random(3)
                if strategy == 0:
                    return gawibwibo[babo_random(3)]
                elif strategy == 1:
                    del gawibwibo[try_index_last_game]
                    return gawibwibo[babo_random(2)]
                else:
                    return gawibwibo[babo_random(3)]


def show_me_the_hand2(records):
    from random import choice
    from random import shuffle
    from random import sample
    from random import randrange
    gawibwibo = ['gawi', 'bawi', 'bo']

    if len(records) == 0:
        return choice(gawibwibo)
    else:
        last_game_index = len(records) - 1
        try_last_game = records[last_game_index][0]
        result_last_game = records[last_game_index][1]
        try_index_last_game = gawibwibo.index(try_last_game)

        if (randrange(10) + 1) % 3 == 0:
            return choice(gawibwibo)
        else:
            if result_last_game == 0:
                shuffle(gawibwibo)
                # sample(gawibwibo, 2)
                return choice(gawibwibo)
            elif result_last_game == 1:
                if randrange(3) == 0:
                    return choice(gawibwibo)
                else:
                    del gawibwibo[try_index_last_game]
                    return choice(gawibwibo)
            elif result_last_game == -1:
                if randrange(3) == 0:
                    return choice(gawibwibo)
                else:
                    del gawibwibo[try_index_last_game]
                    return choice(gawibwibo)


def test():
    r1 = []
    r2 = []
    win1 = 0
    win2 = 0
    draw = 0
    for i in range(1000):
        h1 = show_me_the_hand(r2)
        h2 = show_me_the_hand2(r1)
        if h1 == h2:
            print('match %d of 1000: tie' % i)
            r = 0
            draw += 1
        elif (h1 == 'gawi' and h2 == 'bo') or (h1 == 'bawi' and h2 == 'gawi') or (h1 == 'bo' and h2 == 'bawi'):
            print('match %d of 1000: p1 win' % i)
            r = 1
            win1 += 1
        else:
            print('match %d of 1000: p2 win' % i)
            r = -1
            win2 += 1

        r1.append((h1, r))
        r2.append((h2, -r))

    print(win1, win2, draw)


if __name__ == '__main__':
    test()
