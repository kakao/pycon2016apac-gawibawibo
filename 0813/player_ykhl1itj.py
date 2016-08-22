import random
import statistics

def show_me_the_hand(records):
    """ possible situations:
    1. Opponent uses random algorithm - determine if the numbers are well-balanced find opponent's least appearing choice
    2. Opponent has pattern - find opponent's pattern and use it against the opponent
    3. Opponent analyzes my record 
    3-1. Opponent chooses what I lose most frequently by
    3-2. Opponent chooses what I win most frequently by
    3-3. Opponent chooses what I choose the most frequently
    Order: Case 2 -> Analyze other cases and score """
    if len(records) < 20:
        return "gawi"
    if opp_choose_win(records, 20):
        myChoice = opp_choose_win_counter(records)
        if len(records) < 50:
            return myChoice
        elif amIWinning:
            assert len(records) > 50
            return myChoice
    # pattern counter
    anal_str = record_to_string(records)
    pattern = find_pattern(anal_str)
    if pattern != "":
        return pattern_counter(pattern)
    # random counter
    if random_analysis(records) < 0.06:
        return random_counter(records)
    else:
        return random.choice(["gawi", "bawi", "bo"])

def find_pattern(anal_str):
    """ find the pattern from checking if there is a repeated pattern at the end """
    pattern = ""
    if len(anal_str) < 6:
        return pattern
    for i in range(3, int(len(anal_str)/2)):
        poss_pat = anal_str[-i:len(anal_str)]
        if poss_pat == anal_str[-i*2:-i]:
            pattern = poss_pat
            break
    return pattern       

def record_to_string(records):
    """ gawi is 's', bawi is 'r', bo is 'p' """
    anal_str= ""
    for rec in records:
        if rec[0] == "gawi":
            anal_str += 's'
        elif rec[0] == "bawi":
            anal_str += 'r'
        elif rec[0] == "bo":
            anal_str += 'p'
    return anal_str

def str_to_choice(string):
    if string == "s":
        return "gawi"
    elif string == "r":
        return "bawi"
    else:
        return "bo"

def pattern_counter(pattern):
    """ return counter to the pattern """
    opp_next_str = pattern[0]
    if opp_next_str == "s":
        return "bawi"
    elif opp_next_str == "r":
        return "bo"
    elif opp_next_str == "p":
        return "gawi"

def opp_stat(records):
    gawiNum, bawiNum, boNum = 0, 0, 0
    for rec in records:
        if rec[0] == "gawi":
            gawiNum += 1
        elif rec[0] == "bawi":
            bawiNum += 1
        elif rec[0] == "bo":
            boNum += 1
    return [("gawi", gawiNum/len(records)), ("bawi", bawiNum/len(records)), ("bo", boNum/len(records))]

def opp_score(records):
    oppScore = 0
    for rec in records:
        if rec[1] == -1:
            oppScore += 0
        elif rec[1] == 0:
            oppScore += 1
        elif rec[1] == 1:
            oppSocre += 3

def random_analysis(records):
    oppStats = opp_stat(records)
    stDev = statistics.stdev(data[1] for data in oppStats)
    return stDev

def random_counter(records):
    oppStats = opp_stat(records)
    oppStats = sorted(oppStats, key = lambda x:x[1])
    myChoiceList = [oppStats[0][0], oppStats[1][0]]
    #myChoice = random.choice(myChoiceList)
    myChoice = myChoiceList[0]
    return myChoice

def opp_choose_win(records, test_len):
    test_rec = records[:test_len]
    oppStat = opp_stat(test_rec)
    bawiNum = oppStat[1][1]
    if bawiNum > test_len * 1 / 2:
        return True
    else:
        return False

def myScore(opp_score):
    if opp_score == 3:
        return 0
    elif opp_score == 1:
        return 1
    else:
        return 3

def opp_choose_win_counter(records):
    gawiSum, bawiSum, boSum = 0, 0, 0
    for rec in records:
        if rec[0] == "gawi":
            gawiSum += myScore(rec[1])
        elif rec[0] == "bawi":
            bawiSum += myScore(rec[1])
        else:
            boSum += myScore(rec[1])
    statList = [('gawi', gawiSum), ('bawi', bawiSum), ('bo', boSum)]
    statList = sorted(statList, key = lambda x:x[1])
    if statList[0][0] == "gawi":
        return "bo"
    elif statList[0][0] == "bawi":
        return "gawi"
    else:
        return "bawi"

def amIWinning(records):
    oppScore, myScore = 0, 0
    for rec in records:
        oppScore += opp_score(records)
        myScore += myScore(opp_score(records))
    if oppScore > myScore:
        return False
    else:
        return True

#print(find_pattern("123454123454123454123454123454123454123454123454123454123454123454123454123454123454123454123454123454123454123454"))
#record = [("gawi", 1), ("bawi", 0), ("bo", -1), ("gawi", 1), ("bawi", 0), ("bo", -1), ("gawi", 1), ("bawi", 0), ("bo", -1), ("gawi", -1)]
#h = show_me_the_hand([("gawi", 1), ("bawi", 0), ("bo", -1), ("gawi", 1), ("bawi", 0), ("bo", -1), ("gawi", 1), ("bawi", 0), ("bo", -1), ("gawi", -1)])
#print(random_analysis(record))
#print(h)
