import random


record = [('gawi', 0)]
def show_me_the_hand(records):

    results = []

    if len(records) == 0:
        t = random.randint(0, 1000)
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