"""
상대플레이어의 직전까지의 경기기록을 전달 받는다
gawi, bawi, bo 중의 하나를 리턴하는 show_me_the_hand를 작성

경기기록
[(가위바위보, 승무패), ...]

"""

from random import choice

def changeListToTupleList(records):
    rrs = []
    for idx, r in enumerate(records):
        if idx %2 == 0:
            rrs.append((records[idx], records[idx + 1]))
    return rrs

def show_me_the_hand(records):
    """
    첫번째는 랜덤
    내가 이긴 경우는(records -1) 그냥 계속 똑같은거 냄
    내가 비겼더나 진경우는(records 1 or 0) 상대방의 전적을 보고 승리의 가능성이 높은 녀석을 낸다
    """

    # 첫판
    if len(records) == 0:
        return choice(['gawi', 'bawi', 'bo'])
    else:
        if type(records[0]) == type(''):
            records = changeListToTupleList(records)

        # 지난번에 내가 이겼나 졌나
        last = records[-1]
        to_win = {'gawi': 'bawi', 'bawi': 'bo', 'bo': 'gawi'}

        # 이긴 경우는 같은거 냄
        if last[1] < 0:
            return to_win[last[0]]

        # 비겼거나 진경우는 상대의 전적을 분석하여 승률이 높은 녀석으로 냄

        # 상대의 누적 전적 쌓는 녀석
        gbb_dict = {'gawi':0, 'bawi':0, 'bo':0}

        for r in records:
            gbb_dict[r[0]] += r[1]

        min = 0
        defeatKey = 'gawi' # 일단 가위로... 잘못되면 가위만 나올듯
        for k,v in gbb_dict.items():
            if min > v:
                min = v
                defeatKey = k

        return to_win[defeatKey]


