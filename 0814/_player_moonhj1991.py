import time


class Player:
    def __init__(self):
        self.hands = ['gawi', 'bawi', 'bo']
        self.gawi = 0
        self.bawi = 0
        self.bo = 0

    def show_me_the_hand(self, records):
        if len(records) < 50:
            hand = self.hands[int(time.time() * 1000000) % 3]
            if hand == 'gawi':
                self.gawi += 1
            elif hand == 'bawi':
                self.bawi += 1
            elif hand == 'bo':
                self.bo += 1
            return hand
        else:
            if min([self.gawi, self.bawi, self.bo]) == self.gawi:
                self.gawi += 1
                return 'gawi'
            elif min([self.gawi, self.bawi, self.bo]) == self.bawi:
                self.bawi += 1
                return 'bawi'
            elif min([self.gawi, self.bawi, self.bo]) == self.bo:
                self.bo += 1
                return 'bo'