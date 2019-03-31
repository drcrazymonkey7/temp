#!/usr/bin/env python
from mpd import MPDClient

client = MPDClient()               # create client object
client.timeout = 200               # network timeout in seconds (floats allowed), default: None
client.idletimeout = None
print("Connecting...")
client.connect("localhost", 6600)
print("Connected!")
return client


MPDClient.playlistadd(abbey, "spotify:album:0ETFjACtuP2ADo6LFhL6HN")

MPDClient.load(abbey[, start:end])

