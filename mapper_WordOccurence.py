#!/usr/bin/python

# sairampr
# skothapa

import sys
import string



# top words for NYtimes data
top_words = ['game','year','first','season','time','team','last','new','player','point']

# top words for Common crawl data
#top_words = ['game','team','player','first','season','year','run','point','league','play']

# top words for Twitter data
#top_words = ['golf', 'basketball', 'baseball', 'tennis', 'nfl', 'game', 'team', 'play', 'player', 'day']

for ipdata in sys.stdin:
        ipdata = ipdata.strip()
       # split the line into words
        words = ipdata.split()
	
	for i in range(len(words)-1):
		x = words[i]
		if x in top_words:
			print ("<"+x+","+ words[i+1]+">\t"+str(1))
