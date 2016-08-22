from random import choice
import operator

def show_me_the_hand(records):
    if len(records) < 100:
        return choice(['gawi', 'bawi', 'bo'])
    
    score = dict(gawi=0, bawi=0, bo=0)

    for hand, win in records:
        score[hand] += win
    
    sorted_score = sorted(score.items(), key=operator.itemgetter(1) or choice([-1, 1]))

    return sorted_score[0][0]