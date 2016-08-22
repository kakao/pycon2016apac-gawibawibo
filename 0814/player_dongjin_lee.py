

hands = {'gawi': 0, 'bawi': 1, 'bo': 2}
handslist = ['gawi', 'bawi', 'bo']
win_hands = ['bawi', 'bo', 'gawi']

temp = 0
temp2 = 0


def show_me_the_hand(records):
    if len(records) == 0:
        return win_hands[0]
    enemyrecords = [x[0] for x in records]
    myrecords = [handslist[(hands[x[0]] - x[1]) % 3] for x in records]

    status = [0, 0, 0]

    for record in enemyrecords:
        status[hands[record]] += 1

    if len(records) > 2:
        for i in range(3):  # 하나만 내기 대응
            if status[i] > 2 and status[(i + 1) % 3] == 0 and status[(i + 2) % 3] == 0:
                return win_hands[i]

    if len(records) > 3:
        flag = 1
        for i in range(3):  # 따라 내기 대응
            if enemyrecords[i] != myrecords[i + 1]:
                flag *= 0
        if flag == 1:
            return win_hands[hands[myrecords[0]]]

    if status[0] == status[1] == status[2]:
        global temp
        temp = (temp + 1) % 3
        return win_hands[temp]
    else:
        for i in range(3):
            if status[i] >= status[(i + 1) % 3] and status[i] >= status[(i + 2) % 3]:
                if status[(i + 1) % 3] > status[(i + 2) % 3]:
                    return win_hands[(i + 2) % 3]
                elif status[(i + 1) % 3] < status[(i + 2) % 3]:
                    return win_hands[(i + 1) % 3]
                else:
                    global temp2
                    temp2 = (temp2 + 1) % 2
                    return win_hands[(i + 1 + temp2) % 3]

    global temp
    temp = (temp + 1) % 3
    return win_hands[temp]  # 버그가 있을때 None이 안나오게
