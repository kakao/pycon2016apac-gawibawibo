
def show_me_the_hand(records):
    sosu = []
    number = 2
    iter = (len(records) % 219*2) + 1
    count = 0

    while True:
        
        isSosu = True
        
        for i in sosu:    
            if number % i == 0:
                isSosu = False
                break
        
        if isSosu:
            count += 1
            sosu.append(number)
        
            if count == iter:
                break
        
        number += 1
        
    listChoice = ['gawi', 'bawi', 'bo']
    number = (number + iter) % 3
    
    return listChoice[number]