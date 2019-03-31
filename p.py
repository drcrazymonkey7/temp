#!/usr/bin/env python
from mpd import MPDClient

def load(uri):
    client = MPDClient()
    client.timeout = 200
    client.idletimeout = None
    client.connect("localhost", 6600)
    client.add(uri)
    client.play()

load("spotify:album:7gmak9ZGm10y4PtZa9SBQn")