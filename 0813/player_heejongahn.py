from random import choice


def show_me_the_hand(records):
    num_gawi, num_bawi, num_bo = return_counts(records)
    num_games = len(records)

    # Random chioce if record isn't large enough
    if num_games <= 3:
        return choice(["gawi", "bawi", "bo"])

    # Choose counter if record is considerably biased
    if num_gawi >= 0.75 * num_games:
        return "bawi"

    if num_bawi >= 0.75 * num_games:
        return "bo"

    if num_bo >= 0.75 * num_games:
        return "gawi"

    # Counter the next hand if choices are repeated
    if if_repeated(records):
        next_hand = records[-3][0]

        if next_hand == 'bawi':
            return "bo"
        elif next_hand == 'gawi':
            return "bawi"
        else:
            return "gawi"

    # Otherwise suppose balanced stragety
    least_frequent_hand = min(num_gawi, num_bawi, num_bo)

    if least_frequent_hand == 'bawi':
        return "bo"
    elif least_frequent_hand == 'gawi':
        return "bawi"
    else:
        return "gawi"


def return_counts(records):
    num_bawi, num_gawi, num_bo = 0, 0, 0
    for hand, result in records:
        if hand == 'gawi':
            num_gawi += 1
        elif hand == 'bawi':
            num_bawi += 1
        else:
            num_bo += 1

    return num_gawi, num_bawi, num_bo


def if_repeated(records):
    num_games = len(records)

    if num_games <= 5:
        return False

    for i in (3, 4, 5):
        prev = records[i - 3]
        while (i < num_games):
            if prev[0] != records[i][0]:
                return False
            else:
                prev = records[i]
                i += 3

    return True
