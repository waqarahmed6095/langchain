import os

import requests
import tweepy
from dotenv import load_dotenv

load_dotenv()

twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
)


def scrape_user_tweets(username, num_tweets=5, mock: bool = False):
    """Scrape a Twitter user's original tweets (i.e.  not retweets or replies) and return them as a list of dictionary.
    Each dictionary has three fields: "time posted" (relative to now), "text" and "url".
    """
    print("hello")
    tweet_list = []
    if mock:
        tweets = requests.get(
            "https://gist.githubusercontent.com/waqarahmed6095/70511cc1fe1ecefb9f44b1e636e9a382/raw/9381812dec549341072134462eda917a1ecafd78/eden-marco-tweets.json",
            timeout=10,
        ).json()

    else:
        try:
            user_id = twitter_client.get_user(username=username).data.id
            tweets = twitter_client.get_users_tweets(
                id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
            )
        except:
            tweets={}
    for tweet in tweets:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":
    tweets = scrape_user_tweets(username="EdenEmarco177")
    print(tweets)
