from collections import Counter
from datetime import datetime

hands = ['gawi', 'bawi', 'bo']
solution = {'gawi':'bawi', 'bawi':'bo', 'bo':'gawi'}
def show_me_the_hand(records=None):
    len_records = len(records)
    if(len_records < 101):
        if(len_records) > 4:
            recent_records = [r[0] for r in records[-4:]]
            if(len(set(recent_records)) == 1):
                you = list(set(recent_records))[0]
                return solution.get(you)
        else:
            my_hand = hands[int(datetime.utcnow().timestamp()*100000) % 3]
            return solution.get(my_hand)
    elif(len_records > 100):
        recent_records = [r[0] for r in records[-4:]]
        if(len(set(recent_records)) == 1):
            you = list(set(recent_records))[0]
            return solution.get(you)
        else:
            my_hand = hands[int(datetime.utcnow().timestamp()*100000) % 3]
            return solution.get(my_hand)
    elif(700 < len_records <= 5000):
        store = [r[0] for r in records]
        return solution.get(Counter(store).most_common()[0][0])
    elif(5000< len_records <= 8000):
        my_hand = hands[int(datetime.utcnow().timestamp()*100000) % 3]
        return solution.get(my_hand)
    elif(8000 < len_records):
        store = [r[0] for r in records]
        return solution.get(Counter(store).most_common()[0][0])
    else:
        my_hand = hands[int(datetime.utcnow().timestamp()*100000) % 3]
        return solution.get(my_hand)  