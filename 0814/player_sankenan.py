game = {"gawi": 0,"bo":0,"bawi":0}
def show_me_the_hand(records):
    try:
        if records[0][0] == -1:
            gmae[records[0]]+=1
        elif records[0][0] == 1:
            gmae[records[0]]-=1
        else:
            gmae[records[0]]+=0

        data = max(max(game["gawi"],game["bo"]),game["bawi"])
        for key, value in ages.items():
            if data == value:
                return key
    except:
        return "bo"