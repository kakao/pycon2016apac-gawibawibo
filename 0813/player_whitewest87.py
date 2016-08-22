def show_me_the_hand(records):
    from random import choice
    import random
    now_turn = len(records)
    if now_turn <= 50:
        return choice(['gawi', 'bawi', 'bo'])
    
    hist = [0,0,0]
    for rec in records:
        if (rec[0] == 'gawi'):
            hist[0] += 1
        elif (rec[0] == 'bawi'):
            hist[1] += 1
        else :
            hist[2] += 1

    target =  random.randint(1,now_turn)
    if ( target <= hist[0] ):
        return 'bawi'
    elif (target <= hist[0] + hist[1]):
        return 'bo'
    else :
        return 'gawi'
