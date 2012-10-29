#!/usr/bin/env python

"""
This script first finds all people you follow and the people they follow. 
Among these people, it finds people who are often followed, but who you don't 
follow. This helps people discover who to follow.

Requires tweepy library
"""

import tweepy
import time
import sys
from tweetutils import *

#variable settings
FRIENDS_LIMIT= 200 #how many friends at most do we extract from one person
WAIT_TIME= 1 #in seconds, between API calls
MAX_DEPTH= 2 #max depth to consider. User is depth 0. I don't recommend value higher

#get user to explore as input
if len(sys.argv)<2:
    START_USER= raw_input("Enter user to explore: ")
else:
    START_USER= sys.argv[1]

#authenticate using OAUTH
api= authenticate()

#initializations
network=[(START_USER, 0)] #tuples of person, depth
graph=[] #lets just store all edges of this graph
counts={} #number of times we see a user come up, ever
color={} #color of every person. 1= currently in Q. 2=explored
failed=[] #users we failed to get tweets for. Maybe they are protected
i=0
while len(network)>0:
    i=i+1

    #pop a person
    user, depth= network.pop(0)
    color[user]= 2 #mark user as explored

    #only want to go up to depth MAX_DEPTH. Don't explore these people anymore
    if depth>=MAX_DEPTH: continue

    #make sure we have enough API calls
    R= 10
    try:
        limits= api.rate_limit_status()
        R= limits['remaining_hits']
    except:
        pass

    #getting 100 people = 1 API call...
    while R<=FRIENDS_LIMIT/100+1:
        time.sleep(60) #wait a minute
        try:
            limits= api.rate_limit_status()
            R= limits['remaining_hits']
        except:
            pass
        print "Waiting to get more API calls... %s" % (time.asctime(time.localtime(time.time())), )

    #explore this user's followers
    try:
        #get all friends, but only those with friend counts <200. The other people are weird
        if depth==0: friends=[friend.screen_name for friend in tweepy.Cursor(api.friends, id=user).items()]
        else: friends=[friend.screen_name for friend in tweepy.Cursor(api.friends, id=user).items(FRIENDS_LIMIT)]
    except:
        #forget them, can happen if timeline private etc
        friends=[]
        print 'Forgetting about user ' + user + '. API call failed.'
        failed.append(user)

    #grow the network accordingly
    graph.extend([(user, f) for f in friends])
    novel= [f for f in friends if not f in color] #those that are not yet colored are novel people

    #keep track of everyone we see, and how many times
    for f in friends: counts[f]= counts.get(f,0)+1 

    print "%d: explored %s at depth %d --Q size: %d. new people found: %d/%d" %(i, user, depth, len(network), len(novel), len(friends))
    network.extend([(n, depth+1) for n in novel])
    for p in novel: color[p]= 1 #currently in Q
    
    #print some preliminary results to user
    if i%5==0:
      mine= [v for (u,v) in graph if u==START_USER]
      recomm= [(counts[p], p) for p in counts if not p in mine]
      recomm.sort(reverse=True)
      
      # print top 20 best
      print "Top 20 preliminary progress report:"
      for (v, p) in recomm[:min(20,len(recomm))]: print "You're not following %s but other %d of your followers are!" % (p, v)
    
    if WAIT_TIME>0: time.sleep(WAIT_TIME)

#give the recommendations
mine= [v for (u,v) in graph if u==START_USER]
recomm= [(counts[p], p) for p in counts if not p in mine]
recomm.sort()
for (v, p) in recomm: print "You're not following %s but other %d of your followers are!" % (p, v)

print 'The following people were not processed because of error:'
for x in failed: print x
print 'ALL DONE!'

