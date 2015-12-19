#!/usr/bin/env python
import argparse, r_flag, p_flag

def handle_requests(parser, args):
    'This takes the args from the cli and controls appropriate functions'
    if args.random:
        r_flag.get_random_item(args.random[0])
    if args.playlist:
        p_flag.rand_playlist(args.playlist[0])
