from random import choice

def show_me_the_hand(records):

    length=len(records)
    
    answer = ""

    if(length % 3 == 0):
        answer = 'gawi'
    else:
        answer = 'bawi'

    return choice([answer,'bo'])