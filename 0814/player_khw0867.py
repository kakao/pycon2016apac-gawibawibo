import datetime

gawi = 'gawi'
bawi = 'bawi'
bo = 'bo'

def show_me_the_hand(records):
	mine = getMyHands(records)
	nextOne = calcNext(mine)
	return nextOne

def getMyHands(records):
	ret = []
	for (hand, score) in records:
		if score == 0:
			ret.append(hand)
		elif score == 1:
			if hand == 'gawi':
				ret.append('bo')
			elif hand == 'bawi':
				ret.append('gawi')
			else:
				ret.append('bawi')
		else:
			if hand == 'gawi':
				ret.append('bawi')
			elif hand == 'bawi':
				ret.append('bo')
			else:
				ret.append('gawi')
	return ret

def calcNext(myRecords):
	bawiCnt = 0
	gawiCnt = 0
	boCnt = 0
	for record in myRecords:
		if record == 'bawi':
			bawiCnt += 1
		elif record == 'gawi':
			gawiCnt += 1
		else:
			boCnt += 1
	if bawiCnt == gawiCnt and bawiCnt == boCnt:
		return getTimeBaseHand()
	else:
		if bawiCnt < gawiCnt and bawiCnt < boCnt:
			return 'bawi'
		elif gawiCnt < bawiCnt and gawiCnt < boCnt:
			return 'gawi'
		elif boCnt < gawiCnt and boCnt < bawiCnt:
			return 'bo'
		else:
			return getTimeBaseHand()

def getTimeBaseHand():
	now = datetime.datetime.now().microsecond
	val = (now // 100000) % 3
	if val == 0:
		return 'bawi'
	elif val == 1:
		return 'gawi'
	else:
		return 'bo'