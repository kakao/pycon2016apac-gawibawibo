from random import choice

history = []
data = ['gawi', 'bawi', 'bo']


def win_data(other_data):
    if other_data == 'gawi':
        return 'bawi'
    elif other_data == 'bawi':
        return 'bo'
    elif other_data == 'bo':
        return 'gawi'


def show_me_the_hand(records):
    rtn = choice(data)
    try:
        other_player_date = records[len(records) - 1]
        if other_player_date in data:
            history.append(other_player_date)
        elif records[len(records) - 2] in data:
            other_player_date = records[len(records) - 2]
            history.append(other_player_date)

        if len(history) > 3:
            if history[-1] == history[-2] and history[-1] == history[-3]:
                return win_data(history[-1])

        return rtn

    except:
        rtn = choice(data)

    return rtn

