import time
def show_me_the_hand(records):
    li = []
    if len(records)>300:
        for i in range(len(records)):
            li.append(records[i][0])
        ba = li.count("bawi")
        ga = li.count("gawi")
        bo = li.count("bo")
        if ba > (len(records)*0.6):
            return("bo")
        elif bo > (len(records)*0.6):
            return("gawi")
        elif ga > (len(records)*0.6):
            return("bawi")

    salt = int(str(time.time())[-1])%3
    beat1 = ["gawi","bawi","bo"]
    beat2 = ["bawi","bo","gawi"]
    beat3 = ["bo","gawi","bawi"]
    judge = (int(time.time())*len(records))%3
    if judge == 0:
        return beat1[salt]
    elif judge == 1 :
        return beat2[salt]
    else:
        return beat3[salt]