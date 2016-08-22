
def show_me_the_hand(ls):
    choice = ['gawi', 'bawi', 'bo']
    if len(ls) == 0:
        return 'bo'
    else:
        return choice[ls[0][1]%3]

