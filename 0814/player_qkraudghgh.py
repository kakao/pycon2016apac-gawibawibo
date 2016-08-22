def show_me_the_hand(records):
	tempNumber = 0
	for record in records:
		if record[1] == 'gawi':
			tempNumber += 1
		elif record[1] == 'bawi':
			tempNumber += 2
		else:
			tempNumber += 3

	if tempNumber % 3 == 0:
		return 'gawi'
	elif tempNumber % 3 == 1:
		return 'bawi'
	else:
		return 'bo'
