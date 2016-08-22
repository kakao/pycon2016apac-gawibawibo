from datetime import datetime

class MT():
    state = list(range(16))
    idx = 0
    int_max = pow(2,32) - 1

class gbb():
    choice = ['bawi', 'bo', 'gawi']

def ticks(dt):
    return (dt - datetime(1, 1, 1)).total_seconds() * 10000000
def now_tick():
    return int(ticks(datetime.utcnow()))
def hex_to_int(arg):
    return int(hex(arg),16)

MT.state[MT.idx] = now_tick()

def show_me_the_hand(records):
    a = MT.state[MT.idx]
    c = MT.state[(MT.idx+13)&15]
    b = hex_to_int(a^c^(a<<16)^(c<<15)) % MT.int_max
    c ^= hex_to_int((c>>11)) % 1000
    a = MT.state[MT.idx] = hex_to_int(b^c)
    d = hex_to_int(a^((a<<5)&0xDA442D20)) % MT.int_max
    MT.idx = hex_to_int((MT.idx+15)&15)
    a = MT.state[MT.idx]
    MT.state[MT.idx] = hex_to_int(a^b^d^(a<<2)^(b<<18)^(c<<28)) % MT.int_max
    return gbb.choice[MT.state[MT.idx] % 3]