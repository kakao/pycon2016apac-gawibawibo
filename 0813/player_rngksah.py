def calcProbability(records):
    ga=0
    ba=0
    bo=0
    for cur in records:
        if cur == 'gawi':
            ga=ga+1
        elif cur == 'bawi':
            ba=ba+1
        else:
            bo=bo+1
    if ga>=ba and ga>=bo:
        return 'bawi'
    elif ba>=ga and ba>=bo:
        return 'bo'
    else:
        return 'gawi'


def show_me_the_hand(records):
    return calcProbability(records)