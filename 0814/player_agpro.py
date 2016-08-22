def show_me_the_hand(records):
    ga_ = 0
    ba_ = 0
    bo_ = 0
    if len(records)==0:
        return 'bawi'
    for i in range(1000):
        if records[0][i] == 'gawi':
            ga_ = ga_ + 1
        elif records[0][i] == 'bawi':
            ba_ = ba_ + 1
        else:
            bo_ = bo_ + 1

    if ga_ > ba_:
        if ga_ > bo_:
            return 'bawi'
        else:
            return 'gawi'
    elif ba_> bo_:
        return 'bo'
    else:
        return 'gawi'
