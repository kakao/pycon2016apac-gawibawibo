import time

def show_me_the_hand(records):
    l = []
    value = ['bawi', 'bo', 'gawi']
    if len(records):
        for i in range(len(records)):
            l.insert(0, records[i][0])
            print(l) 
            count = [l.count('gawi'), l.count('bawi'), l.count('bo')]
            print(count)
            for j in range(len(count)):
                if max(count) == count[j]:
                    print(j, max(count))
                    return value[j] 
    else:
        return value[int(time.time()) % 3]          


