
def show_me_the_hand(records):
    # 상대방이 지금까지 뭘 냈던 랜덤으로 선택
    records_length = len(records)

    # 50번 까지 데이터 수집
    if records_length <= 100:
        # print("come")
        if records_length % 3 == 0:
            return 'gawi'
        elif records_length % 3 == 1:
            return 'bawi'
        elif records_length % 3 == 2:
            return 'bo'

    else:
        res = calculate_me(records)
        result = calculate_you(records, res)
        return result

def calculate_you(records ,me):
    # 테스트 데이터 분석

    records_len = len(records)

    idx = 0
    cnt = 0
    cnt_win = 0

    for v in records:
        if records[2 * idx] == me:
            if records[2 * idx + 1] == -1:
                cnt = cnt + 1
            if records[2 * idx + 1] == 1:
                cnt_win = cnt_win + 1
        idx = idx + 1
        if 2 * idx + 1>= records_len:
            break

    if cnt_win > cnt:
        return me
    else:
        return absWin(me)


def calculate_me(records):
    # 테스트 데이터 분석

    records_len = len(records)

    idx = 0
    gawi_cnt = 0
    bawi_cnt = 0
    bo_cnt = 0

    for v in records:
        if records[2 * idx + 1] == 1:
            if v == 'gawi':
                gawi_cnt = gawi_cnt + 1
            elif v == 'bawi':
                bawi_cnt = bawi_cnt + 1
            else:
                bo_cnt = bo_cnt + 1
        idx = idx + 1
        if 2 * idx + 1 >= records_len:
            break

    result = bigger(gawi_cnt, bawi_cnt, bo_cnt)
    return result


def bigger(x, y, z):
    if x >= y:
        if x >= z:
            return 'gawi'
        else:
            return 'bo'
    else:
        if y >= z:
            return 'bawi'
        else:
            return 'bo'


def absWin(hand):
    if hand == 'gawi':
        return 'bawi'
    elif hand == 'bawi':
        return 'bo'
    elif hand == 'bo':
        return 'gawi'





