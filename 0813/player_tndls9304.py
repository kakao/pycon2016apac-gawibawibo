import random
def show_me_the_hand(records):
    lists = ['gawi','bawi','bo']
    ratio = 3.1024996
    choose = ''
    ratio_list=[1./ratio,2.1614/ratio,1.01]
    if len(records) % 4 == 1:
        random.shuffle(lists)
    value = random.random()
    for i in range(2):
        if value > ratio_list[i]:
            choose = lists[i]
            break
        else:
            choose = lists[2]
    return choose