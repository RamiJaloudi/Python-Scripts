import json
#import urllib2
import urllib

url = 'http://search.twitter.com/search.json?q=obama'
#data = urllib2.urlopen(url)
data = urllib.urlopen(url)
print data.read()

'''
json_format = json.load(data)
# user a different variable to shorten the name
js = json_format


# print everything out
js


# get the length of the data
len(js)


#get the length of data per pages
len(js['results'])

#now dissect deeper
#first tweet
js['results'][0]['text']
js['results'][2]['text']
#all tweets on this pages
i=0
while i <len(js['results']):
    print js['results'][i]['text'].encode('utf-8')
    i += 1

#more specific data here
#the profile image a twitter user who mentioned Obama
js['result'][3]['profile_image_url_https']
 
#who the tweet came from
js['results'][5]['from_user_name']

js['results'][6]['metadata']
js['results'][4]['profile_image_url']

#you can do more than this!
'''
