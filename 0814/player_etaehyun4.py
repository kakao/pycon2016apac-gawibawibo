HANDS = ['R', 'S', 'P']
Win = {'R': 'P', 'S': 'R', 'P': 'S'}
Lose = {'R': 'S', 'S': 'P', 'P': 'R'}
MAX_COMPARE = 500
recent = 'R'

def to_kor(hand):
	if hand == 'R':
		return 'bawi'
	elif hand == 'S':
		return 'gawi'
	else:
		return 'bo' 

def to_eng(hand):
	if hand == 'bawi':
		return 'R'
	elif hand == 'gawi':
		return 'S'
	else:
		return 'P'

def show_me_the_hand(records):
	global recent
	score = {'R': 0.0, 'S': 0.0, 'P': 0.0}
	score[Win[recent]] += 0.05

	L = len(records)
	countPattern = {'R': 0, 'S': 0, 'P': 0}

	for i in range(1, L):
		for j in range(0, min(L, MAX_COMPARE)):
			if i + j >= L: break
			if records[j][0] != records[i + j][0]: break
			countPattern[Win[to_eng(records[i - 1][0])]] += i

	if sum(countPattern.values()) > 0:
		for key in countPattern:
			score[key] += countPattern[key] / sum(countPattern.values())

	countWin = {'R': 0, 'S': 0, 'P': 0} 
	for i in range(L):
		if records[i][1] == 1:
			for key in countWin:
				if key == Lose[to_eng(records[i][0])]: continue
				countWin[key] += 1

		elif records[i][1] == -1:
			countWin[Win[to_eng(records[i][0])]] += 1
	if sum(countWin.values()) > 0:
		for key in countWin:
			score[key] += countWin[key] * 0.5 / sum(countWin.values())

	max_score = max(score['R'], score['S'], score['P'])
	for key in score:
		if score[key] == max_score:
			recent = key

	return to_kor(recent)