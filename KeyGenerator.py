import random

def key_generator():
	alpha_list = [i for i in range(65,91)] # '65 66 ... 89 90'
	k = []
	for i in range(26):
		k.append(random.choice(alpha_list))
		alpha_list.remove(k[len(k)-1])
	return k