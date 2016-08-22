import time

def show_me_the_hand(records):
	case = int(time.clock()*10000000)%3 
	if case == 0:
		return('bawi')
	elif case == 1:
		return('gawi')
	else:
		return('bo')
