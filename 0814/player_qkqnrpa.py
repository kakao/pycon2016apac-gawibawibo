def show_me_the_hand(records):
    gababo = ['bawi', 'bo', 'gawi']
    if len(records) == 0:
        return gababo[0]
    return gababo[records[0][1]]
