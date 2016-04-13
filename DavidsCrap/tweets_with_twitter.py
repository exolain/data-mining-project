#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------
import pymongo
from twitter import *

db = pymongo.MongoClient().datamining

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {
"access_key" : "129414887-fyyvLxnIAf04nwKuFkaKEYGqs8bBLjfn52Wyvov2",
"access_secret" : "gXY6Cfl0qHOC0zhj0iXPy1ln88pe1oWt2XfdoGA9t8FH7",
"consumer_key" : "le7k6fQQcd1mK0ZiBHSapXBoN",
"consumer_secret" : "ps7tCNLzbHmqPwGJoyTm6cTwQXSQ16scTIGoQqZAS8aXrs2z9a"
}

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------
query = twitter.search.tweets(q = "data analytics", count=100, lang="en")

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
for result in query["statuses"]:
	try:
		created_at = result["created_at"]
		name = result["user"]["screen_name"]
		text = result["text"]
		print "(%s) @%s %s" % (created_at, name, text)
		db.tweets.insert({
			"created" : created_at,
			"name" : name,
			"text": text
			})
	except:
		pass
