from random import choice

preReturn = ''

def show_me_the_hand(records):

	if(len(records) == 0):
		preReturn = choice(['gawi', 'bawi', 'bo'])
		return preReturn
	elif(len(records) >= 1):
		if(records[0] == 'gawi'):
			preReturn = 'bawo'
		elif(records[0] == 'bawi'):
			preReturn = 'bo'
		else:
			preReturn = 'gawi'
		return preReturn