gawi = "gawi"
bawi = "bawi"
bo = "bo"
win = "win"
lose = "lose"

class Player:
    def show_me_the_hand(self, records):
        gawiCount = 0
        bawiCount = 0
        boCount = 0

        for result in records:
            if result[0][0] == gawi:
                gawiCount += 1
            elif result[0][0] == bawi:
                bawiCount += 1
            else:
                boCount += 1

        if gawiCount > bawiCount:
            if (gawiCount > boCount):
                return bo
            else:
                return gawi
        elif bawiCount > boCount:
            return bo
        else:
            return bawi






