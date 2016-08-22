# Written by Youngbin Han <sukso96100@gmail.com>

def show_me_the_hand(records):
	
	select = 0
	items = ['gawi', 'bawi' 'bo']
			
	if(len(records) == 0):
		select = len(records) % 3
		return items[select-1]
		
	last_hand = records[len(records)-1][0]
	last_result = records[len(records)-1][1]
	
	if(last_result==1):
		choose_hand(last_hand)
	elif(last_result==-1):
		return last_hand
	elif(last_result==0):
		select = len(records) % 3
		return items[select-1]
		
def choose_hand(hand):
	if(hand=="gawi"):
		return "bawi"
	elif(hand=="bawi"):
		return "bo"
	elif(hand=="bo"):
		return "gawi"