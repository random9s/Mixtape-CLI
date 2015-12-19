#!/usr/bin/env python
import argparse, json, webbrowser, urllib2, random
from pprint import pprint
ARTIST="artist"
ALBUM="album"
SONG="track"

def get_random_item(item):
    if item == ARTIST:
        get_artist()
    if item == ALBUM:
        get_album()
    if item == SONG:
        get_song()

def get_artist():
    items = []
    artist = []
    while not items:
        url = create_query(ARTIST)
        response = urllib2.urlopen(url)
        data = json.load(response)
        items = data['artists']['items']
    name = items[0]['name']
    aid = items[0]['id']
    name.lstrip()
    aid.lstrip()
    print "You should check out the artist: '%s'" %name

def get_album():
    items = []
    album = []
    while not items:
        url = create_query(ALBUM)
        response = urllib2.urlopen(url)
        data = json.load(response)
        items = data['albums']['items']
    name = items[0]['name']
    print "You should check out the album: '%s'" %name

def get_song():
    None
    items = []
    tracks = []
    while not items:
        url = create_query(SONG)
        response = urllib2.urlopen(url)
        data = json.load(response)
        items = data['tracks']['items']
    name = items[0]['name']
    prev_url = items[0]['preview_url']
    print "Would you like to listen to a preview of '%s'" %name
    print "[Y/N]:",
    opt = raw_input()
    if opt.lower() == 'y':
        webbrowser.open(prev_url)

def create_query(item):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    queries = []
    for i in range(15):
        letter = ''
        letter_count = random.randint(1,2)
        for i in range(letter_count):
            pos=random.randint(0,25)
            hold=alphabet[pos]
            letter+=hold
        queries.append(letter+'%25')
        queries.append('%25'+letter+'%25')
    query = random.choice(queries)
    offset = random.randint(0,500)
    return 'https://api.spotify.com/v1/search?q='+query+'&type='+item+'&market=US&limit=1&offset='+str(offset)
