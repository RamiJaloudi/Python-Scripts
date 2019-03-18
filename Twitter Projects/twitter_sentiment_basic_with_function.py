from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="I0zEQ6TZbNDbQK44kGYbIcdoQ"
csecret="6CabwjLidazguNm6bbhn9TpA1a6zLfbVyzMLkuL518o88Ilh7Y"
atoken="3064499643-6FoYt11LlsuIaDahGJuZDz4w25Ery3lE9B0BPjG"
asecret="uOgt5jHcV1CoQuoHK5uClgkp8IA480h2n3YMDGEfVSLX4"

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
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
