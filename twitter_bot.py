import os as os
import dotenv as dotenv
import time as time
import tweepy as tweepy

import services as _services
from src.services import get_tweet
import unsplash as _unsplash

dotenv.load_dotenv()

API_KEY = os.environ["TWITTER_API_KEY"]
SECRET_KEY = os.environ["TWITTER_API_SECRET_KEY"]
ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]


def _get_twitter_api():
    auth = tweepy.OAuthHandler(API_KEY,SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    twitter_api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return twitter_api


def _write_tweet():
    tweet = _services.get_tweet()
    twitter_api = _get_twitter_api()
    twitter_api.update_status(tweet)

_write_tweet()


def _post_image():
    _unsplash.download_image()
    twitter_api = _get_twitter_api()
    twitter_api.update_status_with_media("picture.jpg")

_post_image()


def run():
    while True:
        _write_tweet()
        time.sleep(1800)
        _post_image()
        time.sleep(1800)

if __name__ == "__main__":
    run()

