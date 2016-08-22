
def show_me_the_hand(records):
    
    try:
        # 처음에는 그냥 하나
        if len(records) == 0:
            return "bawi"

        # 1개만 내는 사람을 처리하기
        gawi = 0
        bawi = 0
        bo = 0

        for i in list(zip(*records))[0]:
            if i == "gawi":
                gawi += 1
            elif i == "bawi":
                bawi += 1
            else :
                bo += 1

        if gawi > bawi + bo:
            return "bawi"
        if bawi > gawi + bo:
            return "bo"
        if bo > gawi + bawi:
            return "gawi"

        # 2개만 내는 사람을 처리하기
        if gawi == 0:
            return "bo"
        if bawi == 0:
            return "gawi"
        if bo == 0:
            return "bawi"

        # 순서가 있는 사람 처리하기
        game_dict = {"gawi": "bawi", "bawi":"bo", "bo":"gawi"}

        if len(records) > 5:
            a = list(zip(*records))[0][-1] != list(zip(*records))[0][-2]
            b = list(zip(*records))[0][-2] != list(zip(*records))[0][-3]
            c = list(zip(*records))[0][-3] != list(zip(*records))[0][-1]
            d = list(zip(*records))[0][-1] == list(zip(*records))[0][-4]
            e = list(zip(*records))[0][-2] == list(zip(*records))[0][-5]
            f = list(zip(*records))[0][-3] == list(zip(*records))[0][-6]

            if a & b & c & d & e & f:
                if len(records) % 3 == 0:
                    return game_dict[list(zip(*records))[0][-1]]
                if len(records) % 3 == 1:
                    return game_dict[list(zip(*records))[0][-2]]                
                if len(records) % 3 == 2:
                    return game_dict[list(zip(*records))[0][-3]]   

        if len(records) % 3 == 0:
            return "gawi"
        if len(records) % 3 == 1:
            return "bawi"
        if len(records) % 3 == 2:
            return "bo"

        return "gawi"
    except:
        if len(records) % 3 == 0:
            return "gawi"
        if len(records) % 3 == 1:
            return "bawi"
        if len(records) % 3 == 2:
            return "bo"


