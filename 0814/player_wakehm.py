
def choice_hand(hand, op):
    """
    hand
        'gawi'
        'bawi'
        'bo'
    op
        'win'
        'lost'
        'eq'
    """

    if hand == 'gawi':
        if op == 'win':
            return 'bawi'
        elif op == 'lost':
            return 'bo'
        else:
            return 'gawi'
    elif hand == 'bawi':
        if op == 'win':
            return 'bo'
        elif op == 'lost':
            return 'gawi'
        else:
            return 'bawi'
    else:
        if op == 'win':
            return 'gawi'
        elif op == 'lost':
            return 'bawi'
        else:
            return 'bo'
        

def show_me_the_hand(history_list):
    win_cnt = 0
    lost_cnt = 0

    for hand in history_list:
        if hand[1] == 1:
            lost_cnt += 1
        elif hand[1] == -1:
            win_cnt += 1
           
    if lost_cnt > 20 and lost_cnt >= win_cnt*1.5: 
        return choice_hand(history_list[0][0], 'eq')

    try:
        # hand lotation
        check_index = 0
        for i, play in enumerate(history_list[1:]):
            if history_list[0][0] == play[0]:
                check_index = i + 1
                break

        if history_list[0][0] == history_list[check_index][0] \
            and  history_list[1][0] == history_list[check_index+1][0] \
            and history_list[2][0] == history_list[check_index+2][0]:
            return choice_hand(history_list[check_index-1][0], 'win')
    except:
        pass

    try:
        # hand eq
        if history_list[0][0] == history_list[1][0] == history_list[2][0]:
            return choice_hand(history_list[check_index-1][0], 'win')
    except:
        pass

    try:
        # hand random
        return choice_hand(history_list[0][0], 'lost')
    except:
        pass

    # etc
    return 'bo'
