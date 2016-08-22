
prime = []
num = 1000
if num >= 2:
    prime.append(2)

for n in range(3, num + 1):
    isprime = True
    for pnum in prime:
        if n % pnum == 0:
            isprime = False
    if isprime == True:
        prime.append(n)



def show_me_the_hand(records):
    if len(records) in prime:
        return 'gawi'
    else:
        if len(records) % 3 == 0:
            return 'bawi'
        else:
            return 'bo'