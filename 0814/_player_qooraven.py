import datetime

__all__ = 'show_me_the_hamds'

HANDS = ['gawi', 'bawi', 'bo']
def show_me_the_hands(records):
    now = datetime.datetime.now()
    try:
        index = now.microsecond % now.second % 3
    except ZeroDivisionError:
        index = 2
    try:
        return HANDS[index]
    except IndexError:
        return HANDS[sum(now.timetuple()) % 3]

