# 제출 소스
from random import choice

def show_me_the_hand(records):
    # 최초 한번은 랜덤...
    if len(records) == 0:
        return choice(['gawi', 'bawi', 'bo'])
    # 이후에는 상대방이 낸 걸 따라내는 플레이어
    if(records[-1]==0):
        return choice(['gawi', 'bawi', 'bo'])
    else :
        return records[-2]
    #return records[0][0]

