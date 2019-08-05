#!/usr/bin/python

# sairampr
# skothapa

import sys

curr_key = None
curr_val = 0

# input comes from STDIN
for key_val in sys.stdin:
	key,str_val = key_val.split("\t",1)
        # convert str_val (currently a string) to int
	try:
		val = int(str_val)
	except:
		continue
	if(curr_key==key):
		curr_val=curr_val+val;

	# write result to STDOUT
	else:
		if(curr_key is not None):			
			print(curr_key+"\t"+str(curr_val))
		curr_key=key;
		curr_val=val;
print(curr_key+"\t"+str(curr_val))		





