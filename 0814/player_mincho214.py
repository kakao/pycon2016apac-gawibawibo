'''
Created on 2016. 8. 14.

@author: cho
'''
    
his = []

def show_me_the_hand(records):
    
    his.append(records)
    result = 'gawi'
    
    gawiCnt = 1
    bawiCnt = 3
    boCnt = 2
    resultCntList = []
    
    for h in his:
        if h == 'gawi':
            gawiCnt += 1
        elif h== 'bawi':
            bawiCnt += 1
        elif h == 'bo':
            boCnt += 1
    
    resultCntList.append(gawiCnt)
    resultCntList.append(bawiCnt)  
    resultCntList.append(boCnt)
    
    maxIndex = resultCntList.index(max(resultCntList))
    
    if maxIndex == 0:
        result = 'bawi'
    elif maxIndex == 1:
        result = 'bo'
    elif maxIndex == 2:
        result = 'gawi'
    
    return result

    