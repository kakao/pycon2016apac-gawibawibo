from random import choice

def show_me_the_hand(records):
    if len(records) == 0:
        return choice(["gawi","bawi","bo"])
    lose = []
    for i in range(len(records)):
        if records[i][1] == -1:
            lose.append(records[i][0])
    ga = lose.count("gawi")
    ba = lose.count("bawi")
    bo = lose.count("bo")

    if ga > ba and ga > bo :
        return "bawi"
    elif bo > ba and bo > ga :
        return "gawi"
    else :
        return "bo"