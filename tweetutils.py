import tweepy
import sys

def authenticate():
    """
    Authenticates the user with oauth credentials that are specified inside
    file called tconf.
    """

    #extract keys
    try:
	    f= open('tconf', 'r')
	    keys= f.read().split()
	    f.close()
    except Exception, e:
        print e
        print '-----'
        print 'you must put your consumer key,secret and access key,secret into\
               file called tconf, in that order one per line'
        quit()

    #authenticate
    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    api = tweepy.API(auth)
    return api
