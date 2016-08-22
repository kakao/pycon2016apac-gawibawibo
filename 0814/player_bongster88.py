from __future__ import division

def enumy_stats(records):
    """
    상대방이 많이 낸 숫자와 승률 계산하기.
    가위를 낸 총 숫자와 이긴 숫자 계산하기.
    """
    win_count = dict(
        gawi=[0, 0, 0],
        bawi=[0, 0, 0],
        bo=[0, 0, 0],
    )
    for selected, result in records:
        if result == 1:
            win_count[selected][0] += 1
        elif result == 0:
            win_count[selected][0] += 0.3
        
        win_count[selected][1] += 1

        if win_count[selected][1]:
            win_count[selected][2] = win_count[selected][0] / win_count[selected][1]
     
    return win_count

def guess(enumy_stat):
    """
    기본을 gawi로 선택 한 후, 이전 결과를 가지고, 선택하기
    """
    best_selected = 'gawi'
    
    for key, (win, total, percent) in enumy_stat.items():
        if key == best_selected:
            continue
        
        if enumy_stat[best_selected][2] < percent:
            best_selected = key
        elif enumy_stat[best_selected][2] == percent:
            if enumy_stat[best_selected][0] < win:
                best_selected = key
    
    if best_selected == 'gawi':
        return 'bawi'
    elif best_selected == 'bawi':
        return 'bo'
    else:
        return 'gawi'

def show_me_the_hand(records):
    stat_result = enumy_stats(records)
    return guess(stat_result)

# if __name__ == '__main__':
#     from random import choice
#     r1 = []
#     r2 = []
#     win_count = 0
#     for i in range(1000):
#         h1 = choice(['gawi', 'bawi', 'bo'])
#         h2 = show_me_the_hand(r1)

#         if h1 == h2:
#             print('match %d of 1000: tie' % i)
#             r = 0
#         elif (h1 == 'gawi' and h2 == 'bo') or (h1 == 'bawi' and h2 == 'gawi') or (h1 == 'bo' and h2 == 'bawi'):
#             print('match %d of 1000: p1 win' % i)
#             r = 1
#         else:
#             print('match %d of 1000: p2 win' % i)
#             r = -1
#             win_count += 1
        
#         r1.insert(0, (h1, r))
#         r2.insert(0, (h2, -r))
    
#     print('my win count is %d' % win_count)
