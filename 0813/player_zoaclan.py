from random import choice

cnts = {}	
def show_me_the_hand(records):
    info = ['gawi', 'bawi', 'bo']
    if len(records) == 0:
        return choice(info)
    cnts = {}
    what = "" 
    for i, record in enumerate(records):
        if i % 2 == 0: 
            what = record
        else:
	    idx = info.index(what)
            if record == 0:
		    what2 = info[(idx+1)%3]
            elif record == 1:
		    what2 = info[(idx+1)%3]
            else:
		    what2 = info[(idx+1)%3]
            if what2 in cnts:
                cnts[what2] +=1
            else:
                cnts[what2] = 0
            what = ""
    return max(cnts)
