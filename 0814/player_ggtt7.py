#hands = ['gawi', 'bawi', 'bo']
hands = ['bawi', 'bo', 'gawi']

def show_me_the_hand_old(records):
	cnt = len(records)
	my_hand = (cnt + 1) % 2 + 1
	return hands[my_hand]

def show_me_the_hand(records):
	if len(records) == 0:
		cnt = len(records)
		my_hand = (cnt + 1) % 3
		return hands[my_hand]
	history_lst = [list(i) for i in  zip(*records)][0]
	gawi_cnt = history_lst.count('gawi')
	bawi_cnt = history_lst.count('bawi')
	bo_cnt = history_lst.count('bo')
	#print (gawi_cnt, bawi_cnt, bo_cnt)
	gawi_cnt2 = history_lst[:20].count('gawi')
	bawi_cnt2 = history_lst[:20].count('bawi')
	bo_cnt2 = history_lst[:20].count('bo')
	if bo_cnt2 >= 10:
		return 'gawi'
	elif gawi_cnt2 >= 10:
		return 'bawi'
	elif bawi_cnt2 >= 10:
		return 'bo'
	elif min(gawi_cnt, bawi_cnt, bo_cnt) == gawi_cnt and gawi_cnt > 10:
		return 'bawi'
	elif min(gawi_cnt, bawi_cnt, bo_cnt) == bawi_cnt and bawi_cnt > 10:
		return 'bo'
	elif min(gawi_cnt, bawi_cnt, bo_cnt) == bo_cnt and bo_cnt > 10:
		return 'gawi'
	else:
		cnt = len(records)
		my_hand = (cnt + 1) % 3
		return hands[my_hand]


if __name__ == '__main__':
	records = []
	records.insert(0,('gawi', 1))
	records.insert(0,('bo', 1))
	records.insert(0,('bawi',0))
	#print ([list(i) for i in  zip(*records)][0])
	#print (records)
	print (show_me_the_hand(records))


