#!/usr/bin/env python
from mpd import MPDClient

client = MPDClient()
client.timeout = 200
client.idletimeout = None
client.connect("localhost", 6600)
client.clear()
client.add("spotify:album:0ETFjACtuP2ADo6LFhL6HN")
client.play()
