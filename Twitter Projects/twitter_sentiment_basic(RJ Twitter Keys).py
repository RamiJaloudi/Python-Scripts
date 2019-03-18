from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey="r2I3FdcFB3WRKpKoxhpb9pkra"
csecret="Snt0LzxPyKIUQphTQmbsf0DKPALKPfCAy4Jjr3g9O3A93AGdHM"
atoken="18894514-JsJsbjRkWF4jgA7nrMyNYfLR3RccNSUlTzrYO5shJ"
asecret="BhFpvR3ZJe46wmA3sEUJ1eStz8y83WtgIlw91jJBU01z6"

class listener(StreamListener):

##with open("links.csv", "w") as file:
##            for link in br.links():
##                newurl = urlparse.urljoin(link.base_url,link.url)
##                b1 = urlparse.urlparse(newurl).hostname
##                b2 = urlparse.urlparse(newurl).path
##                newurl =  "http://"+b1+b2
##                file.write(newurl+"\n")
##                # print newurl
    def on_data(self, data):
##        text1 = data
##        with open('sample2.txt', 'wt') as f:
##            f.write(text1)
        print(data)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["laws"])
