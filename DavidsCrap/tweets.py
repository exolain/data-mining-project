#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream, API, Cursor

#Variables that contains the user credentials to access Twitter API 
access_token = "129414887-fyyvLxnIAf04nwKuFkaKEYGqs8bBLjfn52Wyvov2"
access_token_secret = "gXY6Cfl0qHOC0zhj0iXPy1ln88pe1oWt2XfdoGA9t8FH7"
consumer_key = "le7k6fQQcd1mK0ZiBHSapXBoN"
consumer_secret = "ps7tCNLzbHmqPwGJoyTm6cTwQXSQ16scTIGoQqZAS8aXrs2z9a"


#This is a basic listener that just prints received tweets to stdout.
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        # It will give 401 if you clock is not up-to-date
        print(status)
        return True

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['text', 'data', 'mining'])



    # api = API(auth)
    # for status in Cursor(api.home_timeline).items(10):
    #     # Process a single status
    #     print(status._json) 