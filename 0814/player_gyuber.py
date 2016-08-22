
hand = ['gawi', 'bawi', 'bo']
my_hand = ""
my_hand_index = 0
my_lose_count = 0
def show_me_the_hand(records):
    global hand
    global my_hand
    global my_hand_index
    global my_lose_count
    if len(records) == 0:
    	my_hand = hand[my_hand_index]
        return my_hand
    if records[0][1] == 1 :
        my_lose_count = 0
        my_hand_index = ( my_hand_index + 1 ) % 3
        my_hand = hand[my_hand_index]
        return my_hand
    else :
        my_lose_count = my_lose_count + 1
        if my_lose_count >= 3 :
            my_hand_index = ( my_hand_index + 1 ) % 3
            my_hand = hand[my_hand_index]
        return my_hand
    
