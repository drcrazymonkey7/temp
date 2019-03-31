#!/usr/bin/env python
from mpd import MPDClient

def load(uri):
    client = MPDClient()
    client.timeout = 200
    client.idletimeout = None
    client.connect("localhost", 6600)
    client.add(uri)
    client.play()

uri = input("Enter Spotify URI: ")

load("uri")
