def show_me_the_hand(records):
    gawi_cnt=records.count(('gawi',1)) + records.count(('gawi',-1)) + records.count(('gawi',0))
    bawi_cnt=records.count(('bawi',1)) + records.count(('bawi',-1)) + records.count(('bawi',0))
    bo_cnt=records.count(('bo',1)) + records.count(('bo',-1)) + records.count(('bo',0))
    # print(gawi_cnt, bawi_cnt, bo_cnt)
    max_cnt=max(gawi_cnt,bawi_cnt ,bo_cnt)
    
    if gawi_cnt == max_cnt : 
        return 'bo'
    elif bawi_cnt == max_cnt :
        return 'gawi'
    else :
        return 'bawi'
    
