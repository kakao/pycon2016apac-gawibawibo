'''
Created on 2016. 8. 14.

@author: hong
'''
    
history = []

def show_me_the_hand(records):
    
    history.append(records)
    
    #print(history)
    
    gawiCnt = 0
    bawiCnt = 0
    boCnt = 1
    cntList = []
    
    result = 'bo'
    
    for a in history:
        if a == 'gawi':
            gawiCnt += 1
        elif a == 'bawi':
            bawiCnt += 1
        elif a == 'bo':
            boCnt += 1
    
    cntList.append(gawiCnt)
    cntList.append(bawiCnt)  
    cntList.append(boCnt)
    
    #print(cntList)
    
    maxInx = cntList.index(max(cntList))
    
    #print(maxInx)
    
    if maxInx == 0:
        result = 'bawi'
    elif maxInx == 1:
        result = 'bo'
    elif maxInx == 2:
        result = 'gawi'
    
    return result

    