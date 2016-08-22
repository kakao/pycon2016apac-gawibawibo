def show_me_the_hand(records):
    list_len = len(records)
    # print(list_len)
    # print(list_len % 3)
    if list_len % 3 == 0 : 
        return 'bawi'
    elif list_len % 3 == 1 :
        return 'bo'
    else :
        return 'gawi'
    
