import hashlib
def show_me_the_hand(r):
	return {0:'gawi',1:'bawi',2:'bo'}[int(hashlib.sha384(str(r).encode()).hexdigest(),16)%3]
