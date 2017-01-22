#bot.py

import os
import tweepy, time, sys
from secrets import * 
from nltk.tag import pos_tag
import string
from tweepy import Stream
from tweepy.streaming import StreamListener
import json


class StreamListener(tweepy.StreamListener):
	print "yo"
	def on_status(self, status):
		print "hey"
		try: 
			print "Hello World2"
			data = {}
			location = ""
			exclude = set('!?.,')

			location = status.place

			#with open('questions.json', 'a') as f: 
				
			print status.text
			print status.id
			print status.user.screen_name
			time.sleep(5)

			sentence = status.text.replace('#askYP', '')
			sentence = ''.join(ch for ch in sentence if ch not in exclude)
			tagged_sent = pos_tag(sentence.split())

			targets = [word for word, pos in tagged_sent if pos == 'NN' or pos == 'NNP']

			#with open('questions.json', 'r') as r:
			#	json_decode = json.load(r)
			
			api.update_status('@%s you want' % target[0])
			time.sleep(2)
			#api.update_status('next one yo')
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
	MyStreamListener = StreamListener()
	twitter_stream = Stream(auth, MyStreamListener)
	twitter_stream.filter(track=['#askUUU'])
