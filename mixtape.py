#!/usr/bin/env python
import argparse, request_handler
"""
-------------------
Mixtape v0.1
-------------------
Author: Jake Parham
Github: https://github.com/random9s
Description: This command-line interface is built to simply randomly
             generate individual tracks, albums, or artists.  Once generated,
             the item is saved to the users Spotify 'saved' list.
             Additionally, this can be used to generate a playlist of compeletly
             random tracks.

Known bugs:  None

"""

def main():
    p = argparse.ArgumentParser(description='Spotify CLI -- Get a random band or song', prog='Mixtape' ,version='%(prog)s 0.1')
    p.add_argument('-r', '--random', help='Generate random [artist, album, track]', nargs=1, choices=['artist', 'album', 'track'], metavar='R')
    p.add_argument('-p', '--playlist', help='Generate random playlist with [num] tracks', nargs=1, type=int, choices=range(2,16), metavar='P')
    args = p.parse_args()
    request_handler.handle_requests(p, args)

if __name__ == "__main__":
    main()
