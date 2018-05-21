"""
Streaming APIs give access to (usually a sample of) all tweets as
they published on Twitter.
"""
# The Streaming API only sends out real-time tweets

# Import JSON to deal with twitter wrapper output
import json
import tokens as tokens

# Importing twitter wrapper library
# from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from twitter import OAuth, TwitterStream

oauth = OAuth(tokens.ACCESS_TOKEN, tokens.ACCESS_SECRET, tokens.CONSUMER_KEY,
              tokens.CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
# Iterator = twitter_stream.statuses.sample()
# Iterator = twitter_stream.statuses.filter(track="Google", language="en")
iterator = twitter_stream.statuses.filter(track='eleição', language="pt")

tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    # if 'delete' in tweet:
    #     continue
    # tweet_count +=1
    # print(json.dumps(tweet, indent=4))
    print(json.dumps(tweet))

    if tweet_count <= 0:
        break
