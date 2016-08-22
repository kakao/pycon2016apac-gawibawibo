from random import choice


def show_me_the_hand(records):
    records_length = len(records)

    if records_length <= 0:
        return choice(['gawi', 'bawi', 'bo'])
    else:
        score = records[records_length - 1]
        last_record = records[records_length - 2]

        if score == 1:
            if last_record == 'gawi':
                return 'bawi'
            elif last_record == 'bawi':
                return 'bo'
            else:
                return 'gawi'
        elif score == 0:
            return last_record
        else:
            if last_record == 'gawi':
                return 'bo'
            elif last_record == 'bawi':
                return 'gawi'
            else:
                return 'bawi'
