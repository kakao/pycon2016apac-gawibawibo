from math import exp
from datetime import datetime
class MersenneTwister:
	# To get last 32 bits
	bitmask_1 = (2 ** 32) - 1
	# To get 32. bit
	bitmask_2 = 2 ** 31
	# To get last 31 bits
	bitmask_3 = (2 ** 31) - 1

	def __init__(self,seed):
		"Initialize the generator from a seed"
		self.MT = [0 for i in range(624)]
		self.MT[0] = seed
		self.index = 0
		for i in range(1,624):
			self.MT[i] = ((1812433253 * self.MT[i-1]) ^ ((self.MT[i-1] >> 30) + i)) & self.bitmask_1


	def random(self):
		"""
		Extract a tempered pseudorandom number based on the index-th value,
		calling generate_numbers() every 624 numbers
		"""
		if self.index == 0:
			self.generate_numbers()
		y = self.MT[self.index]
		y ^= y >> 11
		y ^= (y << 7) & 2636928640
		y ^= (y << 15) & 4022730752
		y ^= y >> 18

		self.index = (self.index + 1) % 624
		return y/2**32
	def generate_numbers(self):
		"Generate an array of 624 untempered numbers"
		for i in range(624):
			y = (self.MT[i] & self.bitmask_2) + (self.MT[(i + 1 ) % 624] & self.bitmask_3)
			self.MT[i] = self.MT[(i + 397) % 624] ^ (y >> 1)
			if y % 2 != 0:
				self.MT[i] ^= 2567483615

rng = MersenneTwister(datetime.now().microsecond)

def show_me_the_hand(records):
	if len(records) < 5:
		return s1(records)
	return s4(records)

def s4(records):
	result = [r[0] for r in records]
	gawi,bawi,bo=0,0,0
	for i in result:
		gawi,bawi,bo = gawi*0.95, bawi*0.95, bo*0.95
		score = decay(i)
		gawi += score[0]
		bawi += score[1]
		bo += score[2]
	rand = rng.random() * (exp(gawi) + exp(bawi) + exp(bo))
	if rand < exp(gawi):
		return 'gawi'
	elif rand < exp(gawi) + exp(bawi):
		return 'bawi'
	return 'bo'

def s1(records): # random guess
	return ['gawi', 'bawi', 'bo'][int(rng.random()*3)]


def decay(opp):
	if opp == 'gawi':
		return 0,0.1,-0.1
	if opp == 'bawi':
		return -0.1,0,0.1
	return 0.1,-0.1,0