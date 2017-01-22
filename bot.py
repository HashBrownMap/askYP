#bot.py

import os
import tweepy, time, sys
from secrets import * 

from tweepy import Stream
from tweepy.streaming import StreamListener
from HTMLParser import HTMLParser
import json

class StreamListener(tweepy.StreamListener):
	print "yo"
	def on_status(self, status):
		print "hey"
		try: 
			print "Hello World2"
			data = {}
			location = ""
			data[status.id] = []
			if status.coordinates:
				location = status.coordinates
			data[status.id].append({
				'tweet': status.text,
				'location': location
				})
			with open('questions.json', 'a') as f: 
				print status.text
				if status.coordinates:
					print "coords:", status.coordinates
				print "ID:", status.id
				json.dump(data, f)
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True

	def on_error(self, status):
		print status
		return True


if __name__ == '__main__':
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
	api = tweepy.API(auth)
	print "Hello World"

	MyStreamListener = StreamListener()
	twitter_stream = Stream(auth, MyStreamListener)
	twitter_stream.filter(track=['#askUUU'])
