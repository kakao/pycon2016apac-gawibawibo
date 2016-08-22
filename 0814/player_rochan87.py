# 'gawi', 'bawi', 'bo'
# SELO77
def show_me_the_hand(records):
    try:
        gawi_count = 0
        bawi_count = 0
        bo_count = 0
        for r in records:
            if r[0] == 'gawi':
                if r[1] == 1:
                    gawi_count += 1
            elif r[0] == 'bawi':
                if r[1] == 1:
                    bawi_count += 1
            else:
                if r[1] == 1:
                    bo_count += 1
        if gawi_count > bawi_count and gawi_count > bo_count:
            return 'gawi'
        elif bawi_count > gawi_count and bawi_count > bo_count:
            return 'bawi'
        elif bo_count > gawi_count and bo_count > bawi_count:
            return 'bo'
        else:
            return 'gawi'
    except:
        return 'gawi'