history = ""

def show_me_the_hand(records):
    global history
    choices = ['bawi', 'bo', 'gawi']
    if len(records) == 0:
        return choices[0]
    else:
        history += records[0][0]
        c = abs(hash(history)) % 2
        return choices[c]
