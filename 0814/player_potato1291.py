import pdb

# 'gawi', 'bawi', 'bo'
game_item = {0: 'gawi', 1: 'bawi', 2:'bo'}

def select_strategy(t, rst, change_flag):
    if change_flag:
        if t == 'gawi': return 'bo'
        elif t == 'bawi': return 'gawi'
        else: return 'bawi'
    else:
        if t == 'gawi': return 'bawi'
        elif t == 'bawi': return 'bo'
        else: return 'gawi'

def patt(recs, total):
    result = {
        (1, True): 0, (1, False): 0,
        (0, True): 0, (0, False): 0,
        (-1, True): 0, (-1, False): 0
    }
      
    prev_game = recs[0]
    for r in recs[1:]:
        curr_game = r
        result[ (prev_game[1], prev_game[0] != curr_game[0]) ] += 1
        prev_game = curr_game
    prev_game_type = prev_game[0]
    prev_game_rst = prev_game[1]
    if result[(prev_game_rst, True)] >= result[(prev_game_rst, False)]:
        my_choice = select_strategy(prev_game_type, prev_game_rst, True)
    else:
        my_choice = select_strategy(prev_game_type, prev_game_rst, False)
    return my_choice

# records = [(type, reward), ...]
def show_me_the_hand(records):
    default_choice = 'bawi'
    interesing_area = 20

    # gathering the data
    if len(records) < interesing_area+1:
        return game_item[len(records)%3]

    return patt(records[:interesing_area+1], interesing_area)
