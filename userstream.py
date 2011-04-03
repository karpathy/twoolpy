#!/usr/bin/env python

"""
Streams your timeline
"""

import time
from getpass import getpass
from textwrap import TextWrapper
from twitstream import *
import tweepy
from tweetutils import *

class myListener(StreamListener):
    def on_status(self, status):
        print "%s: %s" %(status.user.screen_name, status.text)

def main():

    api= authenticate()
    listener= myListener(api)
    stream = Stream(api.auth, listener, timeout=None, secure=True)
    stream.userstream()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'


