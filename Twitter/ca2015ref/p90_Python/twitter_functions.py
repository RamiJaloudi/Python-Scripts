import twitter
import util
from config import *

api = twitter.Api(consumer_key=key,consumer_secret=secret,access_token_key=access_key,access_token_secret=access_secret)

def search(searchTerm):
    """
    Print recent tweets containing `searchTerm`.

    To test this function, at the command line run:
        python twitter_api.py --search=<search term>
    For example,
        python twitter_api.py --search=python
    """

    try:
        tweets = api.GetSearch(searchTerm)
    except twitter.urllib2.URLError:
        print ("Unable to connect to network, giving up.")
        twitter.sys.exit()

    if len(tweets) > 15:
        tweets = tweets[:15]

    for tweet in tweets:
        print '@'+tweet.user.screen_name+': ',
        util.safe_print(tweet.GetText())

def trendingTopics(woeid):
    """twitter apisearch 
    Print the currently trending topics.

    To test this function, at the command line run:
        python twitter_api.py -t
    """
    try:
        trending_topics = api.GetTrendsWoeid(woeid)
    except twitter.TwitterError:
        trending_topics = api.GetTrendsCurrent()
    except twitter.urllib2.URLError:
      print ("Unable to connect to network, giving up.")
      twitter.sys.exit()
    for topic in trending_topics:
        util.safe_print(topic.name)

def userTweets(username):
    """
    Print recent tweets by `username`.

    You may find the twitter.Api() function GetUserTimeline() helpful.

    To test this function, at the command line run:
        python twitter_api.py -u <username>
    For example,
        python twitter_api.py -u bostonpython
    """
    try:
        tweets = api.GetUserTimeline(screen_name=username)
    except twitter.TwitterError:
        print ("User @" + username + " not found")
        twitter.sys.exit()
    except twitter.urllib2.URLError:
        print ("Unable to connect to network, giving up.")
        twitter.sys.exit()

    for tweet in tweets:
        util.safe_print(tweet.GetText())

def trendingTweets(woeid):
    """
    Print tweets for all the trending topics.

    To test this function, at the command line run:
        python twitter_api.py -w
    """
    try:
        trending_topics = api.GetTrendsWoeid(woeid)
    except twitter.TwitterError:
        trending_topics = api.GetTrendsCurrent()
    except twitter.urllib2.URLError:
        print ("Unable to connect to network, giving up.")
        twitter.sys.exit()

    for topic in trending_topics:
        print "**",topic.name
        esc_topic_name = twitter.urllib2.quote(topic.name.encode('utf8'))
        tweets = api.GetSearch(esc_topic_name)
        for tweet in tweets[:5]:
            print '@' + tweet.user.screen_name + ': ',
            util.safe_print(tweet.GetText())
        print '\n'
