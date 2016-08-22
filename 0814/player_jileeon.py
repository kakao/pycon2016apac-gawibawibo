def low_cnt_of_hand(records, return_val='score'):
    hand = {
        'gawi': 0,
        'bawi': 0,
        'bo': 0
    }

    for record in records:
        hand[record[0]] += 1
   
    min_val = min(hand.values()) 

    best_hand = []
    for k, v in hand.items():
        if min_val == v:
            best_hand.append(k)

    if return_val == 'hand':
        return best_hand
    else:
        return min_val
    
        
def max_score_of_hand(records, return_val='score'):
    hand = {
        'gawi': 0,
        'bawi': 0,
        'bo': 0
    }

    for record in records:
        hand[record[0]] += record[1]
   
    max_val = max(hand.values()) 

    best_hand = []
    for k, v in hand.items():
        if max_val == v:
            best_hand.append(k)
    
    if return_val == 'hand':
        return best_hand
    else:
        return max_val

def high_cnt_of_winning_hand(records, return_val='score'):
    hand = {
        'gawi': 0,
        'bawi': 0,
        'bo': 0
    }

    for record in records:
        if record[1] == 3:
            hand[record[0]] += 1
   
    max_val = max(hand.values()) 

    best_hand = []
    for k, v in hand.items():
        if max_val == v:
            best_hand.append(k)

    if return_val == 'hand':
        return best_hand
    else:
        return max_val

STRATEGIES = [
    low_cnt_of_hand,
    max_score_of_hand,
    high_cnt_of_winning_hand
]

RELIABILITY = {}
for strategy in STRATEGIES:
    RELIABILITY[strategy.__name__] = 0
LAST_STRATEGY = None
CURRENT_GAME_CNT = 1


def show_me_the_hand(records):
    global RELIABILITY
    global LAST_STRATEGY
    global CURRENT_GAME_CNT
    global STRATEGIES
    
    CURRENT_GAME_CNT  = len(records)    
    if len(records) == 0:
        return 'gawi'

    last_score = records[-1][1]
 
    # Update reliability
    if LAST_STRATEGY is not None:
        if last_score == 3:
            RELIABILITY[LAST_STRATEGY] += len(records)
        else:
            RELIABILITY[LAST_STRATEGY] -= len(records)

    max_score = 0
    best_strategy = None

    # Calculate the score of each strategies
    for strategy in STRATEGIES:
        score = strategy(records)
        
        if best_strategy is not None:
            if max_score == score:
                if RELIABILITY[best_strategy.__name__] < RELIABILITY[strategy.__name__]:
                    best_strategy = strategy
            elif max_score < score:
                max_score = score
                best_strategy = strategy
            else:
                pass
        else:
            best_strategy = strategy
    
    LAST_STATEGY = best_strategy.__name__   
    best_hands = best_strategy(records, return_val='hand')

    if len(best_hands) == 1:
        best_hands[0]
    elif len(best_hands) == 2:
        best_hands[CURRENT_GAME_CNT%2]
    else:  # 3
        best_hands[CURRENT_GAME_CNT%3]

