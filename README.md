Twoolpy: 

Twitter Tools using Tweepy in Python. 

To use:

1. install tweepy:
$ easy_install tweepy
(requires: $ sudo apt-get install python-setuptools)

2. Follow this excellent tutorial to set up oauth access:
http://talkfast.org/2010/05/31/twitter-from-the-command-line-in-python-using-oauth 
Once you register an app on Twitter they will give you 4 strings: consumer key, consumer secret, access key, and access secret. 

3. Create a new file called "tconf" where you keep twoolpy and enter the 4 strings one per line, in order listed above (consumer key, consumer secret, access key, and access secret)

4. run authest.py to make sure everything is setup right. If yes, some people's names will be printed, or error will result



SCRIPTS:

$ python recommend.py blahblah
gives recommendations to user 'blahblah' on who to follow, based on their social graph on twitter. It looks for people who are very often followed by blahblah's followers, but who 'blahblah' doesn't follow. 

$ python userstream.py
displays tweets in the user timeline, live

