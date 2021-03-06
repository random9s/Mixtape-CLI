#!/usr/bin/env python
import os, argparse, json, webbrowser, urllib, urllib2, random
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
    print "Would you like to listen to a track from this artist?"
    print "[Y/N]",
    opt = raw_input()
    if opt.lower() == 'y':
        preview_artist_song(aid)

def get_album():
    items = []
    album = []
    while not items:
        url = create_query(ALBUM)
        response = urllib2.urlopen(url)
        data = json.load(response)
        items = data['albums']['items']
    name = items[0]['name']
    aid = items[0]['id']
    print "You should check out the album: '%s'" %name
    print "Would you like to listen to a preview from this album?"
    print "[Y/N]",
    opt = raw_input()
    if opt.lower() == 'y':
        preview_album_song(aid)

def get_song():
    None
    items = []
    tracks = []
    dest = os.getcwd()+'/audio.mp3'
    while not items:
        url = create_query(SONG)
        response = urllib2.urlopen(url)
        data = json.load(response)
        items = data['tracks']['items']
    name = items[0]['name']
    prev_url = items[0]['preview_url']
    print "Would you like to listen to a preview of '%s'?" %name
    print "[Y/N]:",
    opt = raw_input()
    if opt.lower() == 'y':
        urllib.urlretrieve(prev_url, dest)
        print "Playing..."
        os.system("afplay audio.mp3")
        os.remove(dest)

def preview_artist_song(artistID):
    preview_ids = []
    dest = os.getcwd()+'/audio.mp3'
    url = 'https://api.spotify.com/v1/artists/'+artistID+'/top-tracks?country=US'
    response = urllib2.urlopen(url)
    data = json.load(response)
    for d in data['tracks']:
        prev_url = d['preview_url']
        preview_ids.append(prev_url)
    play_url = random.choice(preview_ids)
    urllib.urlretrieve(play_url, dest)
    print "Playing..."
    os.system("afplay audio.mp3")
    os.remove(dest)

def preview_album_song(albumID):
    preview_ids = []
    dest = os.getcwd()+'/audio.mp3'
    url = 'https://api.spotify.com/v1/albums/'+albumID+'/tracks?country=US'
    response = urllib2.urlopen(url)
    data = json.load(response)
    for d in data['items']:
        prev_url = d['preview_url']
        preview_ids.append(prev_url)
    play_url = random.choice(preview_ids)
    urllib.urlretrieve(play_url, dest)
    print "Playing..."
    os.system("afplay audio.mp3")
    os.remove(dest)

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
