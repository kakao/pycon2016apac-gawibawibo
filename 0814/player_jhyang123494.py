
games = 0

def show_me_the_hand(records):
    global games
    games += 1
    if games <= 333:
        return 'bawi'
    elif games <= 666:
        return 'gawi'
    else:
        return 'bo'
