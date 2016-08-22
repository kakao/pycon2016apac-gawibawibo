# -*- coding: utf-8 -*-
from random import choice


def show_me_the_hand(records):

    # 이전 내역이 없으면 랜덤으로 일단 제시한다.
    if len(records) == 0:
        return choice(['gawi', 'bawi', 'bo'])

    # 내역이 있는 경우 패턴을 분석한다.
    else:
        duplicate_cnt = {
            'gawi': 0,
            'bawi': 0,
            'bo': 0
        }

        prev_status = ''

        is_pattern = False
        # 반복되는 패턴이 있는지 파악한다.
        for record in records:
            status, win = record

            if status == prev_status:

                duplicate_cnt[status] += 1

                # 3번정도 이상 반복되면 반복되는 것이라 판단하고 break
                if duplicate_cnt[status] > 3:
                    is_pattern = True
                    break
                prev_status = status

            else:
                # is_pattern = False
                # # 반복이 되지 않으면 초기화
                # duplicate_cnt = {
                #     'gawi': 0,
                #     'bawi': 0,
                #     'bo': 0
                # }
                prev_status = status

        if is_pattern:
            # 가장 많은 패턴이 나타나는 내용과 반대의 내용을 제출한다.
            pattern = max(duplicate_cnt, key=duplicate_cnt.get)

            return win_result(pattern)

        # 패턴이 아닌 경우에는 일반 경우의 수를 따른다.
        else:

            # 최근 결과에서 값을 가져온다.
            status, win = records[-1]

            # 이전 결과가 이긴 경우에는 계속 그것을 내려는 경향이 있으므로 반대를 낸다.
            if win == 1:
                return win_result(status)

            # 진 경우라면 그것을 제외하고 다른 것을 내려는 경향이 있다. 가정
            elif win == -1:
                if status == 'gawi':
                    # 주먹, 보를 낼 가능성이 있으므로 이기는 방향은:
                    return 'bo'
                elif status == 'bawi':
                    # 가위, 보를 낼 가능성이 있으므로
                    return 'gawi'
                else:
                    # 주먹, 가위를 낼 가능성이 있으므로
                    return 'bawi'

            # 비긴 경우라면 나는 랜덤으로 낸다.
            else:
                return choice(['gawi', 'bawi', 'bo'])


def show_me_the_hand_rand(records):

    return choice(['gawi', 'bawi', 'bo'])


def show_me_the_hand_bawi(records):
    return 'bawi'


def win_result(opposite):

    if opposite == 'gawi':
        return 'bawi'
    elif opposite == 'bawi':
        return 'bo'
    else:
        return 'gawi'
