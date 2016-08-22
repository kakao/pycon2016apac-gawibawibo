import math
import time


def make_fail(hand):
    if hand is 'gawi':
        return 'bo'
    if hand is 'bo':
        return 'bawi'
    if hand is 'bawi':
        return 'gawi'


def make_success(hand):
    if hand is 'gawi':
        return 'bawi'
    if hand is 'bo':
        return 'gawi'
    if hand is 'bawi':
        return 'bo'


def nCr(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)


def compare(list1, list2):
    if len(list1) is not len(list2):
        print(len(list1), len(list2))
        raise "wrong len"
    count = 0
    if not list1:
        return 0.0
    for ele1, ele2 in zip(list1, list2):
        if ele1 == ele2:
            count += 1
    return count


def find_max_interval(history, target):
    max_seq = 10
    n = max_seq
    list_length = len(history)
    if max_seq < list_length:
        n = max_seq
    else:
        n = list_length - 1

    max_r = 0.0
    max_start = 1
    max_finish = list_length - 1
    score = 0
    for compare_length in range(2, n):
        # below just max is for speed. if time limit allow much, just use 0.
        for start_pos in range(max(1, list_length - compare_length * 10), list_length - compare_length):
            # for start_pos in range(0, list_length - compare_length - 1):
            score = compare(history[:compare_length], target[start_pos:start_pos + compare_length])
            r = 0.0
            for i in range(score):
                r += nCr(compare_length, i) * ((1 / 3.0) ** i) * ((2 / 3.0) ** (compare_length - i))
            # if r > 95.0:
            #     return start_pos, start_pos + compare_length, r
            if max_r < r:
                max_r = r
                max_start = start_pos
                max_finish = start_pos + compare_length
    # print("sc", score, "maxr", max_r)
    return max_start, max_finish, max_r


def make_my(pair):
    hand, result = pair
    if result is -1:
        return make_fail(hand)
    elif result is 0:
        return hand
    else:
        return make_success(hand)


def show_me_the_hand(source_list):
    if len(source_list) < 3:
        i = int(time.time() * 100) % 3
        hand_list = ['gawi', 'bawi', 'bo']
        return hand_list[i]
    my_history = list(map(make_my, source_list))

    history, result_history = zip(*source_list)
    fail_history = list(map(make_fail, history))
    win_history = list(map(make_success, history))

    (start_h, finish_h, r_h) = find_max_interval(history, history)
    (start_f, finish_f, r_f) = find_max_interval(history, fail_history)
    (start_w, finish_w, r_w) = find_max_interval(history, win_history)
    (start_m, finish_m, r_m) = find_max_interval(history, my_history)

    # print("his:", source_list)
    # print('fail', fail_history)
    # print('win', win_history)
    # print(start_h, finish_h, r_h)
    # print(start_f, finish_f, r_f)
    # print(start_w, finish_w, r_w)

    if r_f > r_h and r_f > r_w and r_f > r_m:
        return make_success(fail_history[start_f-1])
    elif r_w > r_h and r_w > r_f and r_w > r_m:
        return make_success(win_history[start_w-1])
    elif r_m > r_w and r_m > r_f and r_m > r_h:
        return make_success(my_history[start_m-1])
    else:
        return make_success(history[start_h-1])


if __name__ == "__main__":
    sample1 = ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo'] + \
              ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo'] + \
              ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo'] + \
              ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo'] + \
              ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo'] + \
              ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo'] + \
              ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo'] + \
              ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo'] + \
              ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo'] + \
              ['gawi', 'bawi', 'bo', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'gawi', 'bawi', 'bo']

    sample2 = ['gawi', 'gawi', 'gawi', 'gawi', 'bawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo'] + \
              ['gawi', 'bo', 'gawi', 'gawi', 'bawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo'] + \
              ['gawi', 'gawi', 'gawi', 'gawi', 'bawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo'] + \
              ['gawi', 'bawi', 'gawi', 'gawi', 'bawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo'] + \
              ['gawi', 'gawi', 'gawi', 'gawi', 'bawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo'] + \
              ['gawi', 'bo', 'gawi', 'gawi', 'bawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo'] + \
              ['gawi', 'gawi', 'gawi', 'gawi', 'bawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo'] + \
              ['gawi', 'gawi', 'gawi', 'gawi', 'bawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo'] + \
              ['gawi', 'gawi', 'gawi', 'gawi', 'gawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo'] + \
              ['gawi', 'gawi', 'gawi', 'gawi', 'bawi', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo', 'bo']
    result = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1] + \
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1] + \
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1] + \
              [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1] + \
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1] + \
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1] + \
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1] + \
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1] + \
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] + \
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
    print(compare(sample1, sample2))
    print(find_max_interval(sample1, sample2))
    print(show_me_the_hand(list(zip(sample1, result))))
    print(show_me_the_hand(list(zip(sample2, result))))
