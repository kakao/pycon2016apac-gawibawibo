import time

def show_me_the_hand(records):
    
    i = int(str(time.time()).ljust(18, '0').replace('.','')[-6:][::-1])%3
    
    return ['gawi', 'bawi', 'bo'][i]