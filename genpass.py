#!/bin/env python

from __future__ import print_function

import argparse

import hashes, backends
from world import *

word_used = ""

def random_word():
    import random
    global word
    word = random.choice(words)  # need some awesome words 
    return word

parser = argparse.ArgumentParser(description="Genpass: Generates passwords to use in IRL")
parser.add_argument("--hash", default="sha512", help="Algorithm to use for example: sha512, random")
parser.add_argument("--service", default="general", help="For generating service specific passwords (default = general)")
parser.add_argument("--backend", default="stdout", help="Saving backend to use for (default = stdout)")
parser.add_argument("--data", default=random_word(), help="Human readable word (default = random word )")
parser.add_argument("--limit", default=0, help="limit length (default = nolimit )")

if __name__== '__main__':
    args = parser.parse_args()

    hash = getattr(hashes, args.hash)
    backend = getattr(backends, args.backend)

    password = hash(args.data, args.service)
    password_with_limit = password[-int(args.limit)::]

    print("Using word : {}, note remember this word".format(word)) 
    print("crypt password generated : {}".format(password_with_limit))
    print("Using Backend : {}".format(args.backend))
    backend({"service": args.service, "hash": args.hash})
