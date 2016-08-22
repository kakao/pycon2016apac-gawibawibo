'''
    writter: third9
'''

import time

def show_me_the_hand(records):
    
    hands = {0:'gawi', 1:'bawi', 2:'bo'}

    # 처음 시작은 가위...
    if len(records) == 0:
        return hands.get(0)

    # 이후에는 상대방이 낸 hand에 따라서
    my_hand = hands.get(0)

    your_hand, r = records[-1]
    if r == 1:
        return your_hand

    elif r == 0:
        if your_hand == 'gawi':
            my_hand = hands.get(1)
        elif your_hand == 'bawi':
            my_hand = hands.get(2)
        elif your_hand == 'bo':
            my_hand = hands.get(0)
        else:
            my_hand = hands.get(0)

        return my_hand

    else:
        choice = int(int(round(time.time()*1000)%10)%3)
        return hands.get(choice)
