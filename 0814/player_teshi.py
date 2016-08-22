import time

hand_list = [ 'gawi', 'bawi', 'bo' ]


def show_me_the_hand(records):
    try:
        count = {}
        count['gawi'] = 0
        count['bawi'] = 0
        count['bo'] = 0

        for item in records:
            count[item[0]] = count[item[0]] + 1

        min_count = 9999
        name = None
        for item in count.keys():
            if min_count > count[item]:
                min_count = count[item]
                name = item
            elif min_count == count[item]:
                name = name + "," + item

        if name.find(",") > 0:
            name_list = name.split(",")
        else:
            name_list = [name]

        return name_list[int(str(time.time())[-1]) % len(name_list)]

    except Exception, e:
        print str(e)
        return hand_list[int(str(time.time())[-1]) % 3]
     

         
