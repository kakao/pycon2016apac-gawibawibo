import time

choice = ['gawi', 'bawi', 'bo']


def show_me_the_hand(records):
    return choice[int(time.time() % 3)]


if __name__ == '__main__':
    print(show_me_the_hand([('gawi', 1)]))
