from random import choice


class Gawibawibo:
    def __init__(self):
        self.my = choice(['gawi', 'bawi', 'bo'])

    def __eq__(self, your):
        if your == 'gawi':
            self.my = 'bawi'
        elif your == 'bawi':
            self.my = 'bo'
        elif your == 'bo':
            self.my = 'gawi'

        return False

    def __repr__(self):
        return self.my

    def __str__(self):
        return self.my

def show_me_the_hand(records):
    return Gawibawibo()