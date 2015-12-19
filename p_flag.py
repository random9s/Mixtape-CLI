#!/usr/bin/evn python
import argparse, json, urllib2, random
from pprint import pprint

def rand_playlist(num):
    'This function calls rand_item above to generate a random playlist'
    for i in range(num):
        print "Generating track no. %d" %i
        #t_id = rand_item("track")
        #array.append(t_id)
        #generate playlist with spotify API passing list of track ids


