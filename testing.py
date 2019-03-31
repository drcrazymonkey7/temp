#!/usr/bin/env python
from mpd import MPDClient

def connectMPD():
	try:
		client = MPDClient()               # create client object
		client.timeout = 200               # network timeout in seconds (floats allowed), default: None
		client.idletimeout = None
		print("Connecting...")
		client.connect("localhost", 6600)
		print("Connected!")
		return client
	except:
		print('Could not connect to MPD server')

def play(client, plist):
		client.stop()
		client.clear()
		client.add(plist)
		if re.search('playlist',plist):
			client.shuffle()
		client.play()

plist = "spotify:album:0ETFjACtuP2ADo6LFhL6HN"

