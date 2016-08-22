cnts = {}	
def show_me_the_hand(records):
    info = ['gawi', 'bawi', 'bo']
    if len(records) == 0:
        return 'gawi'
    cnts = {}
    what = "" 
    weight = 0
    for i, record in enumerate(records):
        if i % 2 == 0: 
            what = record
        else:
            weight += 1
	    idx = info.index(what)
            if record == 1:
		    what2 = info[(idx)%3]
            else:
		    what2 = info[(idx+1)%3]
            if what2 in cnts:
                cnts[what2] += weight
            else:
                cnts[what2] = 0
            what = ""
    return max(cnts)
