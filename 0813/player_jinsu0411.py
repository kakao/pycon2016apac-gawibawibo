from random import choice, randint
import operator 

def show_me_the_hand(records):
    if not records:
        return choice(['gawi', 'bawi', 'bo'])
    result = dict(gawi=randint(0, 3),bawi=randint(0, 3),bo=randint(0, 3))
    for i in range(len(records), 2):
        name = records[i]
        value = records[i+1]
        result[name] += value
    sorted_result = sorted(result.items(), key=operator.itemgetter(1))
    return sorted_result[2][0]