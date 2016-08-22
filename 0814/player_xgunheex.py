import timeit

def show_me_the_hand(records):
    rand = timeit.timeit('for x in range(100): x=x', number=1000)
    rand = str(rand).replace(".","")[-1:]
    
    if int(rand) > 6:
        hand = "bawi"
    elif int(rand) > 3:
        hand= "gawi"
    else:
        hand="bo"
        
    return hand
    