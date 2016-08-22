import time

def show_me_the_hand(records):
    ret = ""
    goRand = True;
    
    if(len(records) > 3):
        print('hit records')
        before3 = records[-4:-1]
        goRand = False
        
        for i in range(3):
            if(before3[i] != before3[0]):
                goRand = True

    if(goRand):
        print('hit rand')
        a,b = 1,1
        n = int(time.time() * (10 ** 6))%100
        for i in range(n-1):
            a,b = b, a+b
        
        if(a%3 == 0): ret = 'gawi'
        if(a%3 == 1): ret = 'bawi'
        if(a%3 == 2): ret = 'bo'
    else:
        print('hit tactic')
        if(before3[0] == 'gawi'): ret = 'bawi'
        if(before3[0] == 'bawi'): ret = 'bo'
        if(before3[0] == 'bo'): ret = 'gawi'

    return ret



