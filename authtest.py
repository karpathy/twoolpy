import tweepy
import sys

#extract keys
f= open('tconf', 'r')
keys= f.read().split()
f.close()
print 'found keys: ' + `keys`

#authenticate
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth)

#little api test
friends=[friend.screen_name for friend in tweepy.Cursor(api.friends, id='twitter').items(100)]
print 'Twitter follows:'
for f in friends: print f

