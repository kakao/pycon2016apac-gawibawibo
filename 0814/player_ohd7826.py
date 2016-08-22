def check_records_len(records):
	total = 0
	total = len(records)
	return int(total)

def check_records_score(records):
	total = 0
	for i in range(len(records)):
		total += int(records[i][1])
	return int(total)

def first(score,llen,records):
	gbb = ['gawi', 'bawi', 'bo']
	check1 = 0
	check2 = 0
	check3 = 0
	temp_score = 0
	temp0 = llen % 1000
	temp1 = llen % 100
	temp2 = llen % 10
	for i in range(0, temp1):
		temp_score = records[temp0 - temp1 + i]
	temp0 = temp0 - temp1
	temp1 = temp1 - temp2
	haha = gbb[llen%3]
	if temp1 < 11:
		return 'bawi'
	elif (records[temp0 + 11] != 'bo') and (temp1 < 50):
		rea = 0
		check1 += 1
		for i in range(temp2):
			if records[temp0 + 11 + i] != 'bo':
				check1 += 1
			rea += 1

		if (check1 < 4) and (rea > 9):
			return haha
		elif (check1 > 9) and (rea > 9):
			return 'bo'
		elif (check1 > 6) and (rea > 9):
			return 'bo'
		else:
			return haha
	elif ( temp_score < 50 ):
		return 'bawi'
	else:
		return 'gawi'
	return 'gawi'

def final(score,llen,records):
	return first(score,llen,records)

def show_me_the_hand(records):
	gbb = ['gawi', 'bawi', 'bo']
	total_len = 0
	total_score = 0

	total_score = check_records_score(records)
	total_len = check_records_len(records)
	if total_len < 10:
		return 'bawi'
	elif total_len < 65:
		return 'gawi'
	elif ( total_score < 50 ) and ( total_len < 101 ):
		return records[total_len-1][0]
	elif ( total_len < 101 ):
		return 'gawi'
	elif ( total_len < 1001 ):
		win = first( total_score, total_len , records)
		return win
	elif ( total_len < 10001) :
		win = final( total_score, total_len, records)
		return win
	return gbb[total_len%3] # Not Excute! Just try,catch!!! Not Random!!!
