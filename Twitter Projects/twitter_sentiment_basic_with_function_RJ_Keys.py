from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="r2I3FdcFB3WRKpKoxhpb9pkra"
csecret="Snt0LzxPyKIUQphTQmbsf0DKPALKPfCAy4Jjr3g9O3A93AGdHM"
atoken="18894514-JsJsbjRkWF4jgA7nrMyNYfLR3RccNSUlTzrYO5shJ"
asecret="BhFpvR3ZJe46wmA3sEUJ1eStz8y83WtgIlw91jJBU01z6"

##def sentimentAnalysis(text):
##    encoded_text = urllib.quote(text)
   

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        #return(True)
##        tweet = data.split(',"text:"')[1].split('","source')[0]
##
##        saveMe = tweet+'::'+sentimentRating+'\n'
##        output = open('output.txt','a')
##        outpute.write(saveMe)
##        output.close()
##        return True
                

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#target"])
