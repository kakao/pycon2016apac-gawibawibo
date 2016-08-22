# PyCon2016APAC KAKAO challenge
# orange.b.jung@gmail.com

a, b, c = 'gawi', 'bawi', 'bo'
# a, b, c = 'a', 'b', 'c'
HANDS = [a,b,c]

def show_me_the_hand(records):
    recordslen = len(records)
    subsets = [] 

    i=1
    for i in range(1, recordslen//2+1): # 딱 과반수 까지만 iterate 돌면서
        subsets = [tuple(records[i*j:i*(j+1)]) for j in range(int(recordslen//i))] # 크기가 그만한 서브셋 리스트를 만듬

        if len(set(subsets)) == 1 and len(subsets) > 1: # 그러다 패턴이 발견되면
            if recordslen % i * len(subsets) == 0: # 그리고 딱 맞아떨어지면
                return(_get_winning_hand(subsets[0][0])) # 다음 주자는 패턴의 첫번째를 이기는 손

            else: # 딱 맞아떨어지지 않으면 오른쪽 꼭다리가 패턴에 맞는지 체크
                left = subsets[0]
                right = (records[i * len(subsets):recordslen])
                for l in range(len(right)):
                    if left[l] != right[l]: # 하나라도 틀리면 안되고
                        return _get_random_hand(recordslen)
                else: # 제시된 패턴과 맞으면 다음 예상되는 손을 이기는 손
                    return _get_winning_hand(left[len(right)])

    else: # 패턴 길이가 recordslen 반을 넘어가면
        for k in range(i+1, recordslen): # 패턴을 더 늘려가며 오른쪽 꼭다리가 패턴에 맞는지 체크
            left = records[0:k]
            right = records[k: recordslen]
            for l in range(len(right)):
                if left[l] != right[l]:
                    break
            else:
                return _get_winning_hand(left[len(right)])
        else:
                return _get_random_hand(recordslen)

# 랜덤 손을 생성하여 리턴
def _get_random_hand(recordslen):
    return HANDS[(recordslen * recordslen) % 3]

# 인자로 들어온 손을 이기는 손을 리턴
def _get_winning_hand(expected_hand):
    return HANDS[((HANDS.index(expected_hand)) + 1) % 3]
    
if __name__ == "__main__":
    print(show_me_the_hand([])) # gen
    print(show_me_the_hand([a])) # gen
    print(show_me_the_hand([b, b])) # b
    print(show_me_the_hand([a, a, a])) # a
    print(show_me_the_hand([a, b, c, a, b, c, a, b])) # c
    print(show_me_the_hand([a, b, c, a, b, c, b])) # gen
    print(show_me_the_hand([a, b, a, b, a, b, a])) # b
    print(show_me_the_hand([a, b, a, b, a, b, c])) # gen
    print(show_me_the_hand([a, a, c, a, a])) # c
    print(show_me_the_hand([a, a, a, a, a, c])) # gen
    print(show_me_the_hand([a, a, b, b, b, c])) # gen
    print(show_me_the_hand([a, a, c, b, a, a])) # c
    print(show_me_the_hand([a, a, c, b, a, a, c])) # b
    print(show_me_the_hand([a, a, c, b, b, c, a])) # a
