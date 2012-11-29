# Prints number of people you follow who tweeted in last 24 hours

import tweepy
import time
import sys
import os.path
from tweetutils import *
import datetime

if len(sys.argv) < 2: 
	print "specify username in command line! QUITTING"
	sys.exit(0)

user = sys.argv[1]
api = authenticate()

f = [x for x in tweepy.Cursor(api.friends, id=user).items()] # User objects

dnow = datetime.datetime.now()
btime = []
for u in f:
	if 'status' in u.__dict__:
		lastDate = u.status.created_at
		dayAgo = dnow - datetime.timedelta(days=1)
		if lastDate > dayAgo:
			btime.append((lastDate, u.screen_name))

btime.sort()
for a in btime: 
	print '%s tweeted last on %s' % (a[1], a[0])

print "%d/%d of the people you follow tweeted in the last 24 hours" % (len(btime), len(f))
