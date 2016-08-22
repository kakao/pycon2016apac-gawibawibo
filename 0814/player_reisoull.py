def show_me_the_hand(records):
    hands = ['gawi', 'bawi', 'bo']

# 연속3번 나오면 그걸 이기는거
    if records[0][0] == records[1][0] and\
        records[0][0] == records[2][0]:
        return hands[(hands.index(records[0][0])+1)%3]

# 상대방이 이긴 카운트가 전체카운트의 반이 넘으면(즉 나보다 이기고 있으면)
# 상대방이 가장 많이 이긴거를 이기는거
    win_data = list(filter(lambda x:x[1] == 1, records))
    win_count = len(win_data)
#    print(win_count)
#    print(len(records)/2.0)
    if win_count > len(records)/2.0:
        tmp_data = list(map(lambda x:x[0], win_data))
        count_list = [('gawi', tmp_data.count('gawi')), ('bawi', tmp_data.count('bawi')), ('bo', tmp_data.count('bo'))]
        sorted(count_list, key=lambda x:x[1])
#        print(count_list)
        return hands[(hands.index(count_list[0][0])+1)%3]

# 아무것도 해당하지 않으면 보를 낸다
    return 'bo'

#test = [('gawi', -1),('bawi', 1),('gawi', -1), ('bo', 1),('bawi', 0),('gawi', 0),('gawi', 1),('gawi', -1),('gawi', 0),('bawi', 1),('bo', 1)]
#print(test)
#print(show_me_the_hand(test))
