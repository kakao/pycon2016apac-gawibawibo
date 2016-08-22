from random import choice

jun_is_same_hand_method = False
jun_is_copycat_method = False
jun_is_hard_copycat_method = False

jun_my_records = []


def show_me_the_hand(records):
    global jun_is_same_hand_method
    global jun_is_copycat_method
    global jun_is_hard_copycat_method
    global jun_my_records

    if len(records) == 0:
        my_hand = choice(['gawi', 'bawi', 'bo'])
        jun_my_records += [my_hand]

        return my_hand

    if jun_is_same_hand_method is False and int(len(records)) >= 100:
        hand = ""
        count = 0

        for item in records:
            if hand == "":
                hand = item[0]
            elif hand is item[0]:
                count += 1

        if count >= 80:
            jun_is_same_hand_method = True

    if jun_is_copycat_method is False and int(len(records)) >= 100:
        count = 0
        for i in range(2, 100):
            if jun_my_records[i - 2] == 'bawi' and records[i - 1][0] == 'bawi':
                count += 1
            elif jun_my_records[i - 2] == 'gawi' and records[i - 1][0] == 'gawi':
                count += 1
            elif jun_my_records[i - 2] == 'bo' and records[i - 1][0] == 'bo':
                count += 1

        if (float(count) / float(len(records))) * 100.0 >= 70.0:
            jun_is_copycat_method = True

            print("copycat")

    if jun_is_hard_copycat_method is False and int(len(records)) >= 100:
        count = 0
        for i in range(2, 100):
            if jun_my_records[i - 2] == 'bawi' and records[i - 1][0] == 'bo':
                count += 1
            elif jun_my_records[i - 2] == 'gawi' and records[i - 1][0] == 'bawi':
                count += 1
            elif jun_my_records[i - 2] == 'bo' and records[i - 1][0] == 'gawi':
                count += 1

        if (float(count) / float(len(records))) * 100.0 >= 70.0:
            jun_is_hard_copycat_method = True

            print("copycat hard")

    if jun_is_same_hand_method is True:
        if records[int(len(records) - 1)][0] == 'bawi':
            my_hand = 'bo'
            jun_my_records += [my_hand]

            return my_hand
        elif records[int(len(records) - 1)][0] == 'gawi':
            my_hand = 'bawi'
            jun_my_records += [my_hand]

            return my_hand
        elif records[int(len(records) - 1)][0] == 'bo':
            my_hand = 'gawi'
            jun_my_records += [my_hand]

            return my_hand
    elif jun_is_copycat_method is True:
        if jun_my_records[int(len(jun_my_records)) - 1] == 'bawi':
            my_hand = 'bo'
            jun_my_records += [my_hand]

            return my_hand
        elif jun_my_records[int(len(jun_my_records)) - 1] == 'gawi':
            my_hand = 'bawi'
            jun_my_records += [my_hand]

            return my_hand
        elif jun_my_records[int(len(jun_my_records)) - 1] == 'bo':
            my_hand = 'gawi'
            jun_my_records += [my_hand]

            return my_hand
    elif jun_is_hard_copycat_method is True:
        if jun_my_records[int(len(jun_my_records)) - 1] == 'bawi':
            my_hand = 'gawi'
            jun_my_records += [my_hand]

            return my_hand
        elif jun_my_records[int(len(jun_my_records)) - 1] == 'gawi':
            my_hand = 'bo'
            jun_my_records += [my_hand]

            return my_hand
        elif jun_my_records[int(len(jun_my_records)) - 1] == 'bo':
            my_hand = 'bawi'
            jun_my_records += [my_hand]

            return my_hand

    my_hand = choice(['gawi', 'bawi', 'bo'])
    jun_my_records += [my_hand]

    return my_hand
