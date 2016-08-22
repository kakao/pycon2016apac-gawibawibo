from random import choice

def show_me_the_hand(records):
    if len(records) == 0:
        return choice(["gawi", "bawi", "bo"])
    
    s = set()
    for k, v in records:
        s.add(k)
    
    if len(s) == 1:
        hand = s.pop()
        
        if(hand == "gawi"):
            return "bawi"
        elif (hand == "bawi"):
            return "bo"
        elif (hand == "bo"):
            return "gawi"
    
    return choice(["gawi", "bawi", "bo"])
    
    
        




