def show_me_the_hand(recoreds):
	if len(records) == 0:
		return 'bawi'
	if records[0][1] == 1:
		if records[0][0] == 'gawi:
			return 'bawi'
		elif records[0][0] == 'bawi':
			return 'bo'
		else:
			return 'gawi'

	else:
		return records[0][0]
