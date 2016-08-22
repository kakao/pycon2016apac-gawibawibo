def show_me_the_hand(records):
    isChecked_gawi = False
    isChecked_bawi = False
    isChekced_bo = False
    index = len(records)
    
    for hand, result in reversed(records):
        if (hand == 'gawi'):
            isChecked_gawi = True
        if (hand == 'bawi'):
            isChecked_bawi = True
        if (hand == 'bo'):
            isChekced_bo = True

        if(isChecked_gawi and isChecked_bawi):
            return 'gawi'
        elif(isChecked_bawi and isChekced_bo):
            return 'bawi'
        elif(isChekced_bo and isChecked_gawi):
            return 'bo'
        
        index = index - 1
        if (index == 0):
            if(isChecked_gawi):
                return 'bawi'
            elif(isChecked_bawi):
                return 'bo'
            else:
                return 'gawi'
    
    return 'bo'