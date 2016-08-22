from random import choice

def show_me_the_hand(records):
    
    gawi = 0
    bawi = 0
    bo = 0
    
    if len(records) == 0:
        return choice(["gawi", "bawi", "bo"])
    
    if list(zip(*a))[0][-1] == "gawi":
        gawi += 1
    elif list(zip(*a))[0][-1] == "bawi":
        bawi += 1
    else :
        bo += 1
        
    if (gawi == bawi) & (bawi == bo):
        return choice(["gawi", "bawi", "bo"])
    
    if gawi > bawi + bo:
        return "bawi"
    if bawi > gawi + bo:
        return "bo"
    if bo > gawi + bawi:
        return "gawi"
    
    return choice(["gawi", "bawi", "bo"])