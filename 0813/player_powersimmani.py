#-*-encoding: utf-8 -*-
def show_me_the_hand(records):
	t_gawi = 0.0
	t_bawi = 0.0
	t_bo = 0.0
	r_gawi = 0.0
	r_bawi = 0.0
	r_bo = 0.0

	for i in records:
		if (i == "gawi"):
			t_gawi +=1.0
		elif(i=="bawi"):
			t_bawi +=1.0
		else:
			t_bo += 1.0
	tot = t_gawi + t_bawi + t_bo
	recent = 0.0

	if(len(records) >= 20):
		for i in records[-20:-1]:
			if (i == "gawi"):
				r_gawi +=1.0
			elif(i=="bawi"):
				r_bawi +=1.0
			else:
				r_bo += 1.0
	r_tot = r_gawi + r_bawi + r_bo 
	
	ret_gawi = (t_gawi / tot) * 0.2 + (r_gawi/r_tot) * 0.8
	ret_bawi = (t_bawi / tot) * 0.2 + (r_bawi/r_tot) * 0.8
	ret_bo = (t_bo / tot) * 0.2 + (r_bo/r_tot) * 0.8
	max_ret = max([ret_gawi,ret_bawi,ret_bo])

	if (ret_gawi == max_ret):
		return "bawi"
	elif(ret_bawi == max_ret):
		return "bo"
	elif(ret_bo == max_ret):
		return "gawi"
	return "bawi"