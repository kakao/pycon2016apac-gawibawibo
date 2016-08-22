
def show_me_the_hand(records):
    num = len(records)
    if num == 0:
        return 'bawi'
    elif num % 3 == 0:
        return 'gawi'
    elif num % 3 ==1:
        return 'bawi'
    else:
        return 'bo'
