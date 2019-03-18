import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
#from elasticsearch import Elasticsearch

# import twitter keys and tokens
from tweepy_config import *

# create instance of elasticsearch
#es = Elasticsearch()

'''
class TweetStreamListener(StreamListener):
    def on_data1(self, data):
        #print(data)
        #return(True)
        tweet = data.split(',"text:"')[1].split('","source')[0]
'''

class TweetStreamListener(StreamListener):
    # on success
    def on_data2(self, data):
        tweet = data.split(',"text:"')[1].split('","source')[0]

        # decode json
        dict_data = json.loads(data)

        # pass tweet
        tweet = TextBlob(dict_data["text"])

        # output sentiment polarity
        print tweet.sentiment.polarity

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiment
        print sentiment

        saveMe = tweet+'::'+sentiment+'\n'
        output = open('outpute.csv','a')
        outpute.write(saveMe)
        output.close()
        return True

    # on failure
    def on_error(self, status):
        print status
        
'''
        saveMe = tweet+'::'+sentiment+'\n'
        output = open('outpute.csv','a')
        outpute.write(saveMe)
        output.close()
        return True
'''

'''
        # add text and sentiment info to elasticsearch
        es.index(index="sentiment",
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})
        return True
'''
  

    # on failure
##    def on_error(self, status):
##        print status

if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create instance of the tweepy stream
    stream = Stream(auth, listener)

    # search twitter for "congress" keyword
    stream.filter(track=['congress'])
