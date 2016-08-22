import time


def show_me_the_hand(records):
    records_length = len(records)

    nansu = records_length / 2
    mil = int(time.time() * 1000)
    index = (mil + nansu) % 3
    if records_length <= 3:
        return 'bawi'
    else:
        cal = {0: case1(records), 1: case2(records), 2: case3(records), 3: case4(records), 4: case5(records)}
        return cal[index]


def case1(records):
    return 'gawi'


def case2(records):
    records_length = len(records)
    score = records[records_length - 1]
    last_record = records[records_length - 2]

    if score == 1:
        if last_record == 'gawi':
            return 'bawi'
        elif last_record == 'bawi':
            return 'bo'
        else:
            return 'gawi'
    elif score == 0:
        return last_record
    else:
        if last_record == 'gawi':
            return 'bo'
        elif last_record == 'bawi':
            return 'gawi'
        else:
            return 'bawi'


def case3(records):
    return 'bo'


def case4(records):
    records_length = len(records)
    score = records[records_length - 1]
    last_record = records[records_length - 2]

    if score == 1:
        if last_record == 'gawi':
            return 'bo'
        elif last_record == 'bawi':
            return 'gawi'
        else:
            return 'bawi'
    elif score == 0:
        return last_record
    else:
        if last_record == 'gawi':
            return 'bawi'
        elif last_record == 'bawi':
            return 'bo'
        else:
            return 'gawi'


def case5(records):
    return 'bawi'
