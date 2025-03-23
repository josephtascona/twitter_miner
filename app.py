from dotenv import load_dotenv
import os

import tweepy
from tweepy import OAuthHandler

load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=bearer_token)

response = client.get_users_tweets(id="1850280150249984000", max_results=10)
for tweet in response.data:
    print(tweet.text)
