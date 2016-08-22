"""
상대플레이어의 직전까지의 경기기록을 전달 받는다
gawi, bawi, bo 중의 하나를 리턴하는 show_me_the_hand를 작성

경기기록
[(가위바위보, 승무패), ...]

"""

from time import time
from math import ceil

def simple_random_gbb():
    num = ceil(time())
    if num % 3 == 0:
        return 'gawi'
    elif num % 3 == 1:
        return 'bawi'
    else:
        return 'bo'

def changeListToTupleList(records):
    rrs = []
    for idx, r in enumerate(records):
        if idx %2 == 0:
            rrs.append((records[idx], records[idx + 1]))
    return rrs

"""
가위바위보 빈도수 분석 함수
"""

def analizeRecords(records):
    gbb_cnt_dict = {'gawi':0, 'bawi':0, 'bo':0}
    gbb_cum_dict = {'gawi':0, 'bawi':0, 'bo':0}

    for tup in records:
        k,v = tup
        gbb_cnt_dict[k] += 1
        gbb_cum_dict[k] += v

    print (gbb_cnt_dict, gbb_cum_dict)
    return (gbb_cnt_dict, gbb_cum_dict)


def show_me_the_hand(records):
    """
    첫번째는 랜덤
    내가 이긴 경우는(records -1) 그냥 계속 똑같은거 냄
    내가 비겼더나 진경우는(records 1 or 0) 상대방의 전적을 보고 승리의 가능성이 높은 녀석을 낸다
    """
    # 첫판
    if len(records) == 0:
        return simple_random_gbb()
    else:
        # 지난번에 내가 이겼나 졌나
        last = records[0]
        to_win = {'gawi': 'bawi', 'bawi': 'bo', 'bo': 'gawi'}

        # 이긴 경우는 같은거 냄
        if last[1] < 0:
            return to_win[last[0]]

        # 비겼거나 진경우는 상대의 전적을 분석하여 승률이 높은 녀석으로 냄

        # 상대의 누적 전적 쌓는 녀석
        gbb_cnt_dict = {'gawi': 0, 'bawi': 0, 'bo': 0} # 몇번냈나
        gbb_cum_dict = {'gawi': 0, 'bawi': 0, 'bo': 0} # 승점이 몇점인가

        for tup in records:
            k, v = tup
            gbb_cnt_dict[k] += 1
            gbb_cum_dict[k] += v


        min_rate_key = 'gawi' #일단 가위 상대방이 랜덤을 쓸가능성이 크니 젤 빈도수 적은 녀석을 찾기
        min_rate = 1000

        for k, v in gbb_cnt_dict.items():
            if min_rate > v:
                min_rate = v
                min_rate_key = k

        max_point = 0
        max_point_key = 'bawi' # 가위 바위보 중에 승률이 제일 높았던 녀석을 뽑아내서 그녀석을 이길 수 있는 애를 냄
        for k,v in gbb_cum_dict.items():
            if max_point < v:
                max_point = v
                max_point_key = k

        analizeRecords(records)

        # 단순 랜덤에게는 아마도... 이기는 로직임
        return to_win[min_rate_key]


