from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey="I0zEQ6TZbNDbQK44kGYbIcdoQ"
csecret="6CabwjLidazguNm6bbhn9TpA1a6zLfbVyzMLkuL518o88Ilh7Y"
atoken="3064499643-6FoYt11LlsuIaDahGJuZDz4w25Ery3lE9B0BPjG"
asecret="uOgt5jHcV1CoQuoHK5uClgkp8IA480h2n3YMDGEfVSLX4"

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
