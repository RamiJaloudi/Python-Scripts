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

user_tweets = twitter.get_user_timeline(screen_name='nylaws', include_rts=True)

output_search = open("HTML.html", "a")

for tweet in user_tweets:
    tweet['text'] = Twython.html_for_tweet(tweet)
    print tweet['text']
    output_search.write(str(tweet['text']).encode("utf-8")+ "\n")

"""
search = twitter.search(q='python')

output_search = open("HTML.html", "a")

for tweet in search:
    tweet['text'] = Twython.html_for_tweet(tweet)
    search = tweet['text']
    print search
    output_search.write(str(search).encode("utf-8") + "\n")
"""
