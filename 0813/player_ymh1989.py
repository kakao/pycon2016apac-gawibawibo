# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 10:48:13 2016

@author: Minhyun
"""

# 가위바위보
from random import choice 
from random import normalvariate
import collections

#def show_me_the_hand_ex1(records): 
## 나는 주먹만 내!!! 
#    return choice(['gawi', 'bawi', 'bo'])
#    
#def show_me_the_hand_ex2(records): 
## 나는 보만 내!!! 
#    return 'bo'

def show_me_the_hand(records): 
    # intervention
    if len(records) < 10:
        return choice(['gawi', 'bawi', 'bo'])
    # look history
    else:
        tmp = [];
        for i in range(len(records)):
            tmp.append(records[i][0]);
            
        counter=collections.Counter(tmp);
        
        # model normal dist.
        model_gawi_val = normalvariate(-1.0, 0.1);
        model_bawi_val = normalvariate(0.0, 0.1);
        model_bo_val = normalvariate(1.0, 0.1);    
        
        # linear combination
        result_val = (counter['gawi'] * model_gawi_val + 
            counter['bawi'] * model_bawi_val + 
            counter['bo'] * model_bo_val) / len(records);
    
        if ((result_val < 0.75) & (-0.75 < result_val)) :  
            return choice(['bo'])
        elif (result_val <= -0.75):
            return choice(['bawi'])
        else:
            return choice(['gawi'])

    
#r1 = []
#r2 = []
#for i in range(1000):
#    h1 = show_me_the_hand_ex1(r2) # computer
#    h2 = show_me_the_hand(r1) # me
#    if h1 == h2:
#        print ('match %d of 1000: tie'% i) 
#        r = 0
#    elif (h1 == 'gawi' and h2 == 'bo') or (h1 == 'bawi' and h2 == 'gawi') or (h1 == 'bo' and h2 == 'bawi'):
#        print ('match %d of 1000: p1 win'% i)
#        r = 1
#    else:
#        print ('match %d of 1000: p2 win' % i)
#        r = -1
#    r1.append((h1, r))
#    r2.append((h2, -r))
#
#sum_com = 0;
#sum_me = 0;
#for i in range(len(r1)):
#    sum_com += r1[i][1];
#    sum_me += r2[i][1];
#
#print ('point (com) : %d' % sum_com)
#print ('point (me) : %d' % sum_me)