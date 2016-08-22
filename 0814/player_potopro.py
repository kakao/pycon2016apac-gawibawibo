#!/usr/bin/env python3


my_recode = []

def show_me_the_hand(recodes):
    """
    >>> show_me_the_hand([])
    'gawi'

    >>> show_me_the_hand(["gawi", "bawi"])
    'bo'
    """
    rsp = ['gawi', 'bawi', 'bo']

    if recodes:
        # 지금까지 냈던 랜덤으로 선택
        get_your_rsp = recodes[-1]
        if get_your_rsp == rsp[0]:
            result = rsp[1]
        elif get_your_rsp == rsp[1]:
            result = rsp[2]
        elif get_your_rsp == rsp[2]:
            result = rsp[0]
    else:
        result = rsp[0]


    my_recode.append(result)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()