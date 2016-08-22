import time


record = [('gawi', 0)]
def show_me_the_hand(records):

    results = []
    get_integer_from_time = str(time.time()).replace('.', '')
    #@@time.sleep(0.1)
    rand = 0

    for i in get_integer_from_time:
        rand += int(i)

    if len(records) == 0:
        t = rand
        if t % 3 == 0:
            return 'gawi'
        if t % 3 == 1:
            return 'bawi'
        if t % 3 == 2:
            return 'bo'

    for record in records:
        if record[1]  == 1:
            results.append(record[0])

    stats = {
        'bawi': 0,
        'gawi': 0,
        'bo': 0,
    }

    for result in results:
        if result == 'gawi':
            stats['gawi'] += 1
            continue
        if result == 'bawi':
            stats['bawi'] += 1
            continue
        if result == 'bo':
            stats['bo'] += 1
    
    return stats.keys()
