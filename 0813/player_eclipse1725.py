from random import choice

def show_me_the_hand(records):
	total = 0
	for i in range(len(records)):
		total += records[i][1]
	check1 = 0
	check2 = 0
	check3 = 0
	gbb = ['gawi', 'bawi', 'bo']
	if len(records) < 50:
		return 'gawi'
	elif records[0][0] == 'gawi':
		check1 += 1
		if records[1][0] == 'gawi':
			check1 += 1
		if records[2][0] == 'gawi':
			check1 += 1
		if records[3][0] == 'gawi':
			check1 += 1
		if records[4][0] == 'gawi':
			check1 += 1
		if check1 > 4:
			return 'bawi'
		else:
			return 'bo'
	elif records[0][0] == 'bo':
		check2 += 1
		if records[1][0] == 'bo':
			check2 += 1
		if records[2][0] == 'bo':
			check2 += 1
		if records[3][0] == 'bo':
			check2 += 1
		if records[4][0] == 'bo':
			check2 += 1
		if check2 > 4:
			return 'gawi'
		else:
			return 'bo'
	elif records[51][1] != 1:
		check3 += 1
		if records[52][1] != 1:
			check3 += 1
		if records[53][1] != 1:
			check3 += 1
		if records[54][1] != 1:
			check3 += 1
		if records[55][1] != 1:
			check3 += 1
		if records[56][1] != 1:
			check3 += 1
		if check3 > 4:
			return choice(gbb)
		else:
			return 'bo'
	else:
		if len(records) > 200:
			if total < 100:
				return choice(gbb)
			else:
				return 'bo'
		return 'bo'
	return choice(gbb)
