# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 10:48:13 2016

@author: Minhyun Yoo
"""

# 가위바위보
import numpy as np
def show_me_the_hand(records): 
    # intervention
    lucky = 7 * 111;
    np.random.seed(lucky)
    length_records = len(records);
    max_iter = 500;
    if length_records < 2:    
        # Say Man == 'BAWI'
        return 'bawi';
        
    elif ((length_records < max_iter) |
    (1000 < length_records < 1000+max_iter) |
    (5000 < length_records < 5000+max_iter)):
        if records[length_records-1][0] == 'bawi':
            return 'bo';
        elif records[length_records-1][0] == 'bo':
            return 'gawi'
        else:
            return 'bawi';
    
    else:       
        # look history
#        tmp = [];
#        
#        for i in range(length_records):
#            tmp.append(records[i][0]);
#            
#        counter=collections.Counter(tmp);
        
        # random number length
        M = length_records + 5;
            
        # pseudo uniform dist. algo.
        a = 7**4; c = 1;  n = M+3;
        R = np.zeros(n+1); U = np.zeros(n+1); 
        R[0] = 1.; U[0] = R[0] / M;
        
        for i in range(1, n+1):
            R[i] = (a*R[i-1]+c) % M;
            U[i] = R[i] / M;  
        
        np.random.shuffle(U);
        
        result_val = U[length_records-1];        
        
        if result_val <= 1.0/3.0+1e-6:
            return 'bawi'
        elif result_val <= 2.0/3.0+1e-6:
            return 'bo'
        else:
            return 'gawi'
