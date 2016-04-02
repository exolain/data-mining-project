#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = "ZMwsD6TF1p9BDdtmzeAkAHhib"
consumer_secret = "tx8D9yuvEATI6Q8Pzxgxx1sTjSNdfrI3gWTRE3BHwgyzin0QFw"
access_token = "395499069-GK8Z9V5LFE8XAMJOodsj1mncpAs0yJzsVY3jBxyJ"
access_token_secret = "uDZ38z1ZT61O637FeCei6wMdJQCwv9Joa7BqM88UwmbI8"


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

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
