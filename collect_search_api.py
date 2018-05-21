"""
Streaming APIs give access to (usually a sample of) all tweets as
they published on Twitter.
"""
# The Streaming API only sends out real-time tweets

# Import JSON to deal with twitter wrapper output
# import json
import tokens as tokens

# Importing twitter wrapper library
# from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from twitter import Twitter, OAuth

oauth = OAuth(tokens.ACCESS_TOKEN, tokens.ACCESS_SECRET, tokens.CONSUMER_KEY,
              tokens.CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

# Search for latest tweets about "#nlproc"
# twitter.search.tweets(q='eleição')

# Get all the locations where Twitter provides trends service
# Brazil 23424768
# world_trends = twitter.trends.available(_woeid=23424768)
# Brasilia 455819
# world_trends = twitter.trends.available(_woeid=455819)
# Sao Paulo 455827
# world_trends = twitter.trends.available(_woeid=455827)

sfo_trends = twitter.trends.place(_id=23424768)

# print(json.dumps(sfo_trends, indent=4))
# print(json.dumps(twitter.application.rate_limit_status(), indent=4))
