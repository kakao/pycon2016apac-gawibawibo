from random import choice

# 기본적인 choice
def show_me_the_hand(records):
    num_gawi = records.count('gawi')
    num_bawi = records.count('bawi')
    num_bo = records.count('bo')

    number_of_records = len(records)

    if number_of_records < 10:
        return 'gawi'

    if num_gawi > (num_bawi + num_bo):
        return 'bawi'
    elif num_bawi > (num_bo + num_gawi):
        return 'bo'
    elif num_bo > (num_gawi + num_bawi):
        return 'gawi'
    else:
        return 'gawi' # 예상승률33%
