#!/usr/bin/env python
import argparse, json, urllib2, random
from pprint import pprint
UID=1284682175
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


def get_album():
    None
    #items = []
    #url = create_query(ALBUM)

def get_song():
    None
    #items = []
    #url = create_query(SONG)

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
