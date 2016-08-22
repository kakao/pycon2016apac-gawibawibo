import datetime
hands = ['gawi', 'bawi', 'bo']

def show_me_the_hand(records):
    s = datetime.datetime.now() - datetime.datetime.utcfromtimestamp(0)
    smod = int(s.total_seconds() * 10000) % 3
    return hands[smod]

print(show_me_the_hand(1))
