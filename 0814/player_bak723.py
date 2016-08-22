

def w(winner, loser, drawn):
	return 4 * winner + 2 * drawn + loser


def w_(records, hand):
	win = 0
	lose = 0
	draw = 0
	for r in records:
		if r[0] == hand:
			if r[1] == 1:
				win += 1
			elif r[1] == 0:
				draw += 1
			else:
				lose += 1
	return w(win, lose, draw)


def show_me_the_hand(records):
	h = []
	if len(records) == 0:
		return 'bo'

	hands = {
		'gawi': 'bawi',
		'bo': 'gawi',
		'bawi': 'bo'
	}
	weights = {
		'gawi': w_(records, 'gawi'),
		'bawi': w_(records, 'bawi'),
		'bo': w_(records, 'bo')
	}

	maxValue = 0.0
	for k in weights.keys():
		if weights[k] > maxValue:
			maxValue = weights[k]
			h = hands[k]

	return h
