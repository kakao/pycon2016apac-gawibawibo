import os
import hashlib, binascii

my_s = str.encode(os.getcwd() + str(os.getpid()))

def show_me_the_hand(records):
    global my_s
    my_s = hashlib.pbkdf2_hmac('sha256', my_s, b'pycon2016apac', 100)

    return ['gawi', 'bawi', 'bo'][my_s[0] % 3]
