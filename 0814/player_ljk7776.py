hands = ['gawi', 'bawi', 'bo']
def show_me_the_hand(records):
	return hands[len(records) % 3]
