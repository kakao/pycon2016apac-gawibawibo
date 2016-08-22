"""
상대방이 내는 가위바위보에 대해,
Markov Chain 모델을 가정한다.
"""


# 이기는 조합
winning_hand = {
        'gawi': 'bawi',
        'bawi': 'bo',
        'bo': 'gawi'
}

# 상대방 관측 데이터 초기화
opponent_data = {
    'gawi': {
        'gawi': 0,
        'bawi': 0,
        'bo': 0
    },
    'bawi': {
        'gawi': 0,
        'bawi': 0,
        'bo': 0
    },
    'bo': {
        'gawi': 0,
        'bawi': 0,
        'bo': 0
    }
}


def show_me_the_hand(records):
    opponnent_hand = guess_opponent_hand(records)

    # 예측한 가위바위보를 이기는 가위바위보를 제출
    return winning_hand[opponnent_hand]


# 상대방의 가위바위보를 예측
def guess_opponent_hand(records):
    if len(records) < 2:
        # 첫 2판에는 바위
        return 'bawi'
    else:
        # 관측 데이터 업데이트
        last_hand = records[1][0]
        curr_hand = records[0][0]
        opponent_data[last_hand][curr_hand] += 1

        # 상대방 가위바위보 예측
        return max(opponent_data[curr_hand], key=opponent_data[curr_hand].get)
