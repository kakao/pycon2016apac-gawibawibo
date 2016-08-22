import time

hands = ['gawi', 'bawi', 'bo']
winhands = {'gawi' : 'bawi', 'bawi': 'bo', 'bo': 'gawi'}
losehands = {'gawi': 'bo', 'bawi': 'gawi', 'bo': 'bawi'}
myhands = 0


def mytime():
    t = int(time.time()*1000000)
    return hands[(t + myhands) % 3]


def filter2(records):
    total = {'gawi': 0, 'bawi': 0, 'bo': 0}
    for item in records:
        total[item[0]] += 1
    for k, v in total.items():
        if v < len(records)*0.2:
            return k


def find_pattern(records):
    max_pattern_p = 0

    for pattern_length in range(1, int(len(records)/2)+1):
        needle = records[-pattern_length:]
        total = len(records)/float(pattern_length)
        found = 1

        i = -pattern_length*2
        while i > (-len(records)):
            compare = records[i:pattern_length]
            if not compare:
                break
            if needle[0] == compare[0]:
                found += 1
            else:
                break
            i -= pattern_length
        if (found/total) > max_pattern_p:
            max_pattern_p = found/total
            max_pattern = needle
    if max_pattern_p > 0.8:
        return max_pattern[0][0]


def show_me_the_hand(records):
    if len(records) == 0:
        return mytime()
    f2 = filter2(records)
    if f2:
        fixed = losehands[f2]
        return fixed

    pattern = find_pattern(records)
    if pattern:
        return winhands[pattern]

    return mytime()
