def show_me_the_hand(records):
	total = {
		'gawi': 0,
		'bawi': 0,
		'bo': 0,
	}
	for before_hand, before_result in records:
		total[before_hand] += before_result
	
	maximum = max(total['gawi'], total['bawi'], total['bo'])

	if maximum == total['gawi'] :
		return 'bo'
	elif maximum == total['bawi'] :
		return 'gawi'
	elif maximum == total['bo'] :
		return 'bawi'
	else :
		return 'bawi'
