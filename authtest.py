import tweepy
import sys
from tweetutils import *

api= authenticate()

#little api test
friends=[friend.screen_name for friend in tweepy.Cursor(api.friends, id='twitter').items(100)]
print 'Twitter follows:'
for f in friends: print f

