import json
from tweepy import OAuthHandler, StreamListener, Stream

import config as c

MAX_TWEETS = 200

HASHTAGS = ['#MAGA', '#AmericaFirst', '#TeamTrump', '#MakeAmericaGreatAgain',
            '#TrumpTrain', '#BuildTheWall', '#PresidentTrump', '#drainTheSwamp']


class CustomListener(StreamListener):
    ''' Handles data received from the stream. '''

    def __init__(self, api=None):

        super(CustomListener, self).__init__()

        self.number_of_tweets = 0
        self.output_file = c.tweets_file

    def on_data(self, data):
        if self.number_of_tweets < MAX_TWEETS:
            tweet = json.loads(data)
            if not tweet['entities']['urls'] and\
                    not tweet['entities']['user_mentions'] and\
                    not tweet['retweeted'] and not tweet['is_quote_status']:

                with open(self.output_file, 'a') as f:
                    f.write('{}\n'.format(tweet))

                self.number_of_tweets += 1

            return True

        else:
            return False


    def on_error(self, status_code):
        print 'Got an error with status code: {}'.format(status_code)
        return True

    def on_timeout(self):
        print 'Timeout...'
        return True


if __name__ == '__main__':

    auth = OAuthHandler(
        c.twitter['consumer_key'], c.twitter['consumer_secret'])
    auth.set_access_token(
        c.twitter['access_token'], c.twitter['access_token_secret'])

    stream = Stream(auth, CustomListener())
    stream.filter(track=HASHTAGS)
