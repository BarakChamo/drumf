import os
from dotenv import Dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '/..')
os.environ.update(Dotenv('.env'))

twitter = {
    'consumer_key': os.environ.get('CONSUMER_KEY'),
    'consumer_secret': os.environ.get('CONSUMER_SECRET'),
    'access_token': os.environ.get('ACCESS_TOKEN'),
    'access_token_secret': os.environ.get('ACCESS_TOKEN_SECRET')
}

tweets_file = os.environ.get('TWEETS_FILE')
