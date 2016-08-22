#예제2: 최초 한번은 랜덤으로, 이후부터는 상대방이 낸 걸 따라내는 플레이어

def randint(a, b):
    "Return random integer in range [a, b], including both end points."
    return a + randbelow(b - a + 1)

def randbelow(n):
    "Return a random int in the range [0,n).  Raises ValueError if n<=0."
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r

def random_bytes(n):
    "Return n random bytes"
    with open('/dev/urandom', 'rb') as file:
        return file.read(n) 

def choice2(a):
    return randint(1,3)

def show_me_the_hand2(records):
    # 최초 한번은 랜덤...
    a=['gawi', 'bawi', 'bo']
    if len(records) == 0:
        r=int(choice2(['gawi', 'bawi', 'bo']))
        #print (r)
        return a[r-1]
    # 이후에는 상대방이 낸 걸 따라내는 플레이어
    return records[0][0]

for i in range (100):
    print(show_me_the_hand2(""))   
