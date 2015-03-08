from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import urllib, json
import urllib2

ckey = '3FfsKyHKlDWOmpwP57ECPIioY'
csecret = 'dV3ZomRgR255MVlOptOTrJqa6zl9oEpbZDR0c0Cggn9qQM665g'
atoken = '39455623-3OplCdYC436UyjjQU6nCBiDL2IlaPwY0ATqtjrpEm'
asecret = 'HtXvx6zuZzDAODVXVYTfnzoNpDAJwQoLueFhMNZIPHWlw'


sentdexAuth = ""


def sentimentAnalysis(text):
    encoded_text = urllib.quote(text)
    API_Call = "http://sentdex.com/api/api.php?text="+encoded_text+'&auth='+sentdexAuth
    output = urllib.urlopen(API_Call).read()
    print output
    return output

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data['text']

        sentimentRating = sentimentAnalysis(tweet)
        saveMe = tweet + "::" + sentimentRating+'\n'
        output = open("output.csv", "a")
        output.write(saveMe)
        output.close()
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

