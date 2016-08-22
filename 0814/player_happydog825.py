def show_me_the_hand(records):
    calc_list = {'bo': 0, 'bawi':0, 'gawi':0}
    my_intel = {'gawi':'bawi','bawi':'bo','bo':'gawi'}
    for resultval in records:
        calc_list[resultval[0]] += resultval[1]
    my_hand = 'bawi'
    if len(calc_list) != 0 :
        yourMinIndex = 'gawi'
        yourMinValue =  calc_list[yourMinIndex]
        for key, value in calc_list.items():
            if( yourMinValue > value):
                yourMinIndex = key
        my_hand = my_intel[yourMinIndex]
    return my_hand