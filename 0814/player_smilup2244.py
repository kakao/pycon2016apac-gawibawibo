import math
import random

def show_me_the_hand(records) :
    curx = 0
    cury = 0
    gawi_theta = math.pi/6
    gawi_x = math.cos(gawi_theta)
    gawi_y = math.sin(gawi_theta)
    bawi_theta = math.pi * 5 / 6
    bawi_x = math.cos(bawi_theta)
    bawi_y = math.sin(bawi_theta)
    bo_theta = math.pi * 3/ 2
    bo_x = math.cos(bo_theta)
    bo_y = math.sin(bo_theta)
    for record in records :
        if(record[0] == 'gawi') :
            curx += gawi_x
            cury += gawi_y
        elif(record[0] == 'bawi') :
            curx += bawi_x
            cury += bawi_y
        else :
            curx += bo_x
            cury += bo_y
    if(curx == 0) :
        cur_theta = 0
    else :
        cur_theta = math.atan(cury/curx)
    if(curx < 0) :
        cur_theta += math.pi
    cur_theta += math.pi / 2
    if(-math.pi / 6 <= cur_theta <= math.pi/2) :
        return 'bawi'
    elif(math.pi/2 <= cur_theta <= math.pi*7/6) :
        return 'bo'
    else :
        return 'gawi'

