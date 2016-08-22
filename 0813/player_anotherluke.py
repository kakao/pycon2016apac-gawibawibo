import random

gbb = ['gawi', 'bawi', 'bo']

def show_me_the_hand(records):
	if len(records) <= 1:
		return random.chocie(gbb)
	
	idx = gbb.index(records[-1][0])
	if records[-2][0] == records[-1][0]:
		return gbb[(idx + 1) % 3]
	else:
		select = random.randint(0, 1)
		return gbb[select + (select >= idx)]
