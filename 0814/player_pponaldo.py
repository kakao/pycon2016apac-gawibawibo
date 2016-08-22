hands = ['gawi','bawi','bo']
def show_me_the_hand(records):
	default = 1
	prev = records[0]
	for i in prev[0]:
		default += ord(i)
		default += prev[1]
		default =  default%3
	return hands[default]

