def show_me_the_hand(records):

	count_bawi = 0
	count_gawi = 0
	count_bo = 0

	for record in records:
		if (record[0] == 'bawi'):
			count_bawi += 1
		elif (record[0] == 'gawi'):
			count_gawi += 1
		elif (record[0] == 'bo'):
			count_bo += 1

	if (count_bawi == count_gawi and count_gawi == count_bo):
		return 'gawi'

	elif (count_bawi > count_gawi):
		if (count_bawi > count_bo) :
			return 'bo'
		else:
			return 'bo'

	else:
		return 'bawi'