import tweepy, os
from dotenv import load_dotenv

# load credentials from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), "crd.env"))

# Twitter API credentials
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_key = os.environ.get("ACCESS_KEY")
access_secret = os.environ.get("ACCESS_SECRET")

# authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_tweets(hashtag, geocode=None, location=False):
	''' returns 30 most recent tweets, given a hashtag and a geolocation (optional) '''

	tweets_text = ""	

	if location:
		tweets = api.search(q="#" + hashtag, geocode=geocode, count=30)	

	else:
		tweets = api.search(q="#" + hashtag, count=30)	

	for tweet in tweets:
		tweets_text +=  tweet._json['text'] + "\n"

	return tweets_text