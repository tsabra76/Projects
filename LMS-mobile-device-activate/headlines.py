import pyttsx 
import urllib2 
import json 
import time

engine = pyttsx.init()
engine.say('Welcome home, Tarek. Here are today\'s headlines .')
response = urllib2.urlopen('http://ajax.googleapis.com/ajax/services/feed/load?v=1.0&num=8&q=http%3A%2F%2Fnews.google.com%2Fnews%3Foutput%3Drss')
data = json.load(response)
titles = data['responseData']['feed']['entries']

for headline in titles:
	#print headline['title']
	engine.say(headline['title'])

engine.runAndWait()