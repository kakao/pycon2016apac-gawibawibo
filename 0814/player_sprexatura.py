for_rand = 0

test_records = [('gawi', 1),('bawi', 0),('bo', -1)]

def count(records):
    count = {}
    count['gawi'] = 0
    count['bawi'] = 0
    count['bo'] = 0
    
    for record in records:
        if record[0] == 'gawi':
            count['gawi'] = count['gawi'] + 1
        elif record[0] == 'bawi':
            count['bawi'] = count['bawi'] + 1
        else:
            count['bo'] = count['bo'] + 1

    return count

def show_me_the_hand(records):
    global for_rand
    for_rand = for_rand + 1
    _count = count(records)
    if for_rand % 10 == 0:
        print 'gawi'
    
    elif max(_count) == 'bawi': print 'bo'
    elif max(_count) == 'gawi': print 'bawi'
    else: print 'gawi'
    
show_me_the_hand(test_records)
