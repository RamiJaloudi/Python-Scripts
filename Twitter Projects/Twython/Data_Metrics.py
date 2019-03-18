#!/usr/bin/env python

"""

Use Twitter API to grab user information from list of organizations; export text file

Uses Twython module to access Twitter API

"""

import sys
import string
import simplejson
from twython import Twython
import datetime
now = datetime.datetime.now()
day=int(now.day)
month=int(now.month)
year=int(now.year)

t = Twython(app_key='r2I3FdcFB3WRKpKoxhpb9pkra',
            app_secret='Snt0LzxPyKIUQphTQmbsf0DKPALKPfCAy4Jjr3g9O3A93AGdHM',
            oauth_token='18894514-JsJsbjRkWF4jgA7nrMyNYfLR3RccNSUlTzrYO5shJ',
            oauth_token_secret='BhFpvR3ZJe46wmA3sEUJ1eStz8y83WtgIlw91jJBU01z6')

#print t.show_user(screen_name=account_name)


ids = "258402588, 445986121, 1730810174, 302931392"
users = t.lookup_user(user_id = ids)

##details = t.show_user(screen_name = 'nj_laws')


outfn = "twitter_user_data_%i.%i.%i.txt" % (now.month, now.day, now.year)

fields = "id screen_name name created_at url followers_count friends_count statuses_count \ favorites_count listed_count \ contributors_enabled description protected location lang expanded_url".split()

outfp = open(outfn, "w")
outfp.write(string.join(fields, "\t") + "\n") # header

for entry in users:
    #CREATE EMPTY DICTIONARY
    r = {}
    for f in fields:
        r[f] = ""
    #ASSIGN VALUE OF 'ID' FIELD IN JSON TO 'ID' FIELD IN OUR DICTIONARY
    r['id'] = entry['id']
    #SAME WITH 'SCREEN_NAME' HERE, AND FOR REST OF THE VARIABLES
    r['screen_name'] = entry['screen_name']
    r['name'] = entry['name']
    r['created_at'] = entry['created_at']
    r['url'] = entry['url']
    r['followers_count'] = entry['followers_count']
    r['friends_count'] = entry['friends_count']
    r['statuses_count'] = entry['statuses_count']
    r['favourites_count'] = entry['favourites_count']
    r['listed_count'] = entry['listed_count']
    r['contributors_enabled'] = entry['contributors_enabled']
    r['description'] = entry['description']
    r['protected'] = entry['protected']
    r['location'] = entry['location']
    r['lang'] = entry['lang']
    #NOT EVERY ID WILL HAVE A 'URL' KEY, SO CHECK FOR ITS EXISTENCE WITH IF CLAUSE
    if 'url' in entry['entities']:
        r['expanded_url'] = entry['entities']['url']['urls'][0]['expanded_url']
    else:
        r['expanded_url'] = ''
    print r
    print '\n\n'
    #CREATE EMPTY LIST
    lst = []
    #ADD DATA FOR EACH VARIABLE
    for f in fields:
        lst.append(unicode(r[f]).replace("\/", "/"))
    #WRITE ROW WITH DATA IN LIST
    outfp.write(string.join(lst, "\t").encode("utf-8") + "\n")
 
outfp.close()    
