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

#twitter.get_home_timelines()

search = twitter.search(q='#target')

output_search = open("Search_Text.txt", "a")

for entry in search:
    print search
    print "\n\n"
    output_search.write(str(search).encode("utf-8") + "\n")    




