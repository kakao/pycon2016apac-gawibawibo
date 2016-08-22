
def show_me_the_hand( records ) :

    gawiCount = 0
    bawiCount = 0
    boCount = 0

    for record in records :
        if 'gawi' == record[0] :
            if record[1] == 1:
                gawiCount = gawiCount + 1
        elif 'bawi' == record[0] :
            if record[1] == 1:
                bawiCount = bawiCount + 1
        else :
            if record[1] == 1:
                boCount = boCount + 1
    
    maxCount = max( gawiCount, bawiCount, boCount )

    if gawiCount == maxCount :
        hands = 'gawi'
    elif bawiCount == maxCount :
        hadns = 'bawi'
    else :
        hands = 'bo'
        
    return hands

