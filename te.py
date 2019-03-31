#!/usr/bin/env python
from mpd import MPDClient

def load(uri):
    client = MPDClient()
    client.timeout = 200
    client.idletimeout = None
    client.connect("localhost", 6600)
    client.clear()
    client.add(uri)
    client.play()

load(str(input("Enter Spotify URI: ")))