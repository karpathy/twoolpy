
# Twoolpy

Twitter API fun scripts using Tweepy in Python. I'm hoping people can use these 
examples as repository to draw on when they develop their own scripts.

#### Scripts

1. `$ python recommend.py blahblah`: gives recommendations to user 'blahblah' on who to follow, based on their social graph on twitter. It looks for people who are very often followed by blahblah's followers, but who 'blahblah' doesn't follow. 

2. `$ python userstream.py`: prints authenticated user's timeline, live

3. `$ python followersdiff.py`: finds all your followers and saves them to local file. Re-running the script
will do a diff with that file so you can see who followed or unfollowed you 
since last time you ran the script.

#### Installation

1. Install tweepy:
`$ easy_install tweepy`
(requires: `$ sudo apt-get install python-setuptools`)

2. Follow [this excellent tutorial](http://talkfast.org/2010/05/31/twitter-from-the-command-line-in-python-using-oauth) to set up oauth access.

3. Once you register an app on Twitter they will give you 4 strings: consumer key, consumer secret, access key, and access secret. Create a new file called `tconf` in the folder where you keep twoolpy and enter the 4 strings one per line, in order listed above (consumer key, consumer secret, access key, and access secret).

4. run `$ python authest.py` to make sure everything is setup right. If yes, some people's names will be printed, or error will result.

#### Licence

WTFPL licence

