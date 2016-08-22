# huklee's balgorithm fo GBB
import datetime

def randomchoice (arr):
    index = int(datetime.datetime.now().timestamp() * 98.7) % len(arr)
    return arr[index]

def show_me_the_hand(records):
    rlen = len(records)
    if (rlen % 10) % 2 == 0:
        return randomchoice (['gawi', 'bawi', 'bo'])
    else:
        mydict = {}
        for (sel, cnt) in records:
            if mydict.get(sel) == None:
                mydict[sel] = 0
            mydict[sel] += cnt;
        return [key for key in mydict.keys() if mydict[key] == max(mydict.values())][0]