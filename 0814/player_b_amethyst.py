import time

def show_me_the_hand(records):
    play_hand = 'bawi'
    if len(records) == 0:
        return play_hand

    play_hand = choice_hand(records)
    return play_hand

def choice_hand(records):
    result_sum = 0
    hand_sum = 0
    direction = 1
    current_milli_time = round(time.time() * 1000)
    for record in records:
        result_sum = result_sum + (record[1]*direction)
        # if result_sum >10:
        #     direction = direction * -2
        hand_sum = sum_hand(result_sum, record[0])
    print('result_sum : ', result_sum)
    if result_sum < 0:
        result_sum = result_sum * -1
    hand_num = (result_sum + hand_sum + current_milli_time) % 3
    if hand_num == 0:
        return 'gawi'
    elif hand_num == 1:
        return 'bawi'
    else:
        return 'bo'

    return 'gawi'

def sum_hand(sum, hand):
    if hand == 'gawi':
        return sum + 0
    elif hand == 'bawi':
        return sum + 1
    else:
        return sum + 2
