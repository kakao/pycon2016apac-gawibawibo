from random import choice

preReturn = ''

def show_me_the_hand(records):

	if(len(records) == 0):
		preReturn = 'gawi'
		return preReturn
	elif(len(records) >= 1):
		if(records[0] == 'gawi'):
			preReturn = 'bawi'
		elif(records[0] == 'bawi'):
			preReturn = 'bo'
		else:
			preReturn = 'gawi'
		return preReturn