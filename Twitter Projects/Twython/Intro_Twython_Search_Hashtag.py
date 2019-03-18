#!/usr/bin/env python

import sys
import string
import simplejson
from twython import Twython
import datetime
now = datetime.datetime.now()
day=int(now.day)
month=int(now.month)
year=int(now.year)


twitter = Twython(app_key='r2I3FdcFB3WRKpKoxhpb9pkra',
            app_secret='Snt0LzxPyKIUQphTQmbsf0DKPALKPfCAy4Jjr3g9O3A93AGdHM',
            oauth_token='18894514-JsJsbjRkWF4jgA7nrMyNYfLR3RccNSUlTzrYO5shJ',
            oauth_token_secret='BhFpvR3ZJe46wmA3sEUJ1eStz8y83WtgIlw91jJBU01z6')

##search_results = twitter.search(q="#terrorism", rpp="50")

##for tweet in search_results["results"]:
  ##  print "Tweet from @%s Date: %s" % (tweet['from_user'].encode('utf-8'),tweet['created_at'])
  ##  print tweet['text'].encode('utf-8'),"\n"


search = twitter.search(q='#test',   #**supply whatever query you want here**
                  count=100)

tweets = search['statuses']

for tweet in tweets:
  print tweet['id_str'], '\n', tweet['text'], '\n\n\n'


