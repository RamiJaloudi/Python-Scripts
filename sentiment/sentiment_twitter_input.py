import sys
import csv
import tweepy
import matplotlib.pyplot as plt

from collections import Counter
# How to install the following module: pip install aylien-apiclient
from aylienapiclient import textapi


if sys.version_info[0] < 3:
   input = raw_input

## Twitter credentials I
#consumer_key = "r2I3FdcFB3WRKpKoxhpb9pkra"
#consumer_secret = "U9G1vdM0UKknFXzlbMrdUfQK46NJPDG9J1y2gtiNtLG3KkMhzB"
#access_token = "18894514-JsJsbjRkWF4jgA7nrMyNYfLR3RccNSUlTzrYO5shJ"
#access_token_secret = "BhFpvR3ZJe46wmA3sEUJ1eStz8y83WtgIlw91jJBU01z6"


## Twitter credentials II
consumer_key = "Z1lIM5cUszlcjUQIDDUcmC4mm"
consumer_secret = "U9G1vdM0UKknFXzlbMrdUfQK46NJPDG9J1y2gtiNtLG3KkMhzB"
access_token = "18894514-Jan4wNCH1OYYEW2tPdLDPKxkTODB3a2jKr8yBqL5g"
access_token_secret = "	iel7T8us63RCFYGz6RitSn0ypjcPDsoZyxwPUKYP7XluA"





## AYLIEN credentials
application_id = "a7bc5a14"
application_key = "a018533c2f92c924db92e95a63337b55"

## set up an instance of Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## set up an instance of the AYLIEN Text API
client = textapi.Client(application_id, application_key)

## search Twitter for something that interests you
query = input("What subject do you want to analyze for this example? \n")
number = input("How many Tweets do you want to analyze? \n")

results = api.search(
   lang="en",
   q=query + " -rt",
   count=number,
   result_type="recent"
)

print("--- Gathered Tweets \n")

## open a csv file to store the Tweets and their sentiment 
file_name = 'Sentiment_Analysis_of_{}_Tweets_About_{}.csv'.format(number, query)

with open(file_name, 'w', newline='') as csvfile:
   csv_writer = csv.DictWriter(
       f=csvfile,
       fieldnames=["Tweet", "Sentiment"]
   )
   csv_writer.writeheader()

   print("--- Opened a CSV file to store the results of your sentiment analysis... \n")

## tidy up the Tweets and send each to the AYLIEN Text API
   for c, result in enumerate(results, start=1):
       tweet = result.text
       tidy_tweet = tweet.strip().encode('ascii', 'ignore')

       if len(tweet) == 0:
           print('Empty Tweet')
           continue

       response = client.Sentiment({'text': tidy_tweet})
       csv_writer.writerow({
           'Tweet': response['text'],
           'Sentiment': response['polarity']
       })

       print("Analyzed Tweet {}".format(c))

## count the data in the Sentiment column of the CSV file 
with open(file_name, 'r') as data:
   counter = Counter()
   for row in csv.DictReader(data):
       counter[row['Sentiment']] += 1

   positive = counter['positive']
   negative = counter['negative']
   neutral = counter['neutral']

## declare the variables for the pie chart, using the Counter variables for "sizes"
colors = ['green', 'red', 'grey']
sizes = [positive, negative, neutral]
labels = 'Positive', 'Negative', 'Neutral'

## use matplotlib to plot the chart
plt.pie(
   x=sizes,
   shadow=True,
   colors=colors,
   labels=labels,
   startangle=90
)

plt.title("Sentiment of {} Tweets about {}".format(number, query))
plt.show()
