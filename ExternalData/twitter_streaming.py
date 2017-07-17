#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "46351813-ejPy02Sq1ayYDRiSGpfkTIlxRxKAhfi3enp2Ken9M"
access_token_secret = "D5du7s9xBRO2Axiqw87wjWzOPQHVA833cEcCqI0DnouaW"
consumer_key = "WOXP4McxHhQ6fdEfk9hutQxRv"
consumer_secret = "Zq3RGwNTozdiajBH5FystrU87x99dmURHjuqVn9kGmwaHfFIhq"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'maybank', 'cimb', 'hong leong'
    stream.filter(track=['maybank', 'cimb', 'hong leong'])